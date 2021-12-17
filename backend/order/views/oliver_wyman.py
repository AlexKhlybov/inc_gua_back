import os

import requests
from decimal import Decimal
import logging
from rest_framework.response import Response
from django.utils.translation import gettext as _

from entity.models import Beneficiary, Principal
from ..models import OliverWymanModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class OliverWyman(object):
    def __init__(self, init_params):
        self.ow_url = os.getenv('OW_URL')
        self.ow_login = os.getenv('OW_LOGIN')
        self.ow_password = os.getenv('OW_PASSWORD')
        self.supplierInn = init_params['supplierInn']
        self.customerInn = init_params['customerInn']
        self.reportType = 'Y'
        self.token = ''
        self.profileId = int(os.getenv('OW_PROFILEID'))
        self.bankId = int(os.getenv('OW_BANKID'))
        self.envType = "PROD"
        self.isAuto = True
        self.apiKey = "ApIkEy-aPiKeY"
        self.param_request = {"profileId": self.profileId,
                              "bankId": self.bankId,
                              "envType": self.envType,
                              "isAuto": self.isAuto,
                              "reportType": self.reportType,
                              "apiKey": self.apiKey,
                              "supplierInn": self.supplierInn,
                              "customerInn": self.customerInn}
        if 'purchaseNumber' in init_params:
            self.purchaseNumber = init_params['purchaseNumber']
            self.param_request['purchaseNumber'] = self.purchaseNumber
        else:
            self.purchaseNumber = None
        self.headers = {}

    def get_token(self):
        response = requests.post(self.ow_url + '/auth/login', json={'login': self.ow_login,
                                                                    'password': self.ow_password})
        json_response = response.json()
        logger.info(f'token response: {json_response}')
        self.token = json_response['auth_token']
        self.headers = {'Authorization': f'Token {self.token}'}
        logger.info(f'token: {self.token}')
        return {'status_code': response.status_code, 'data': json_response}

    def get_inputs(self, purchaseNumber=''):
        result_token = self.get_token()
        if result_token['status_code'] != 200:
            return {'status_code': result_token['status_code'], 'data': result_token['data']}
        response = requests.post(self.ow_url + '/guarantee/get_inputs',
                                 headers=self.headers,
                                 json=self.param_request)
        json_response = response.json()
        logger.info(f'get_inputs response: {json_response}')
        return {'status_code': response.status_code, 'data': json_response}

    def update_params(self, param_request, response_data):
        added_params = []
        added_params.append('pl2110_d1')
        added_params.append('pl2400_d1')
        added_params.append('pl2110_d2')
        added_params.append('pl2400_d2')
        added_params.append('pl2110_d3')
        added_params.append('pl2400_d3')
        for param in added_params:
            if param in response_data:
                cur_value = response_data[param]
                self.param_request[param] = cur_value
        self.param_request['reportQuarter'] = 2

    def create_response(self, json_response):
        response_data = {}
        response_data['signals'] = json_response['additional_data']['signals']
        response_data['courts'] = json_response['additional_data']['courts']['factors']
        response_data['executory'] = json_response['additional_data']['executory']['factors']
        response_data['tenders'] = json_response['additional_data']['tenders']['factors']
        response_data['score_data'] = json_response['data']
        response_data['finance'] = json_response['additional_data']['finance']
        return response_data

    def get_score_guarantee(self):
        result_inputs = self.get_inputs()
        if result_inputs['status_code'] != 200:
            return {'status_code': result_inputs['status_code'], 'data': result_inputs['data']}
        self.headers = {'Authorization': f'Token {self.token}'}
        param_request = {"profileId": self.profileId,
                         "bankId": self.bankId,
                         "envType": self.envType,
                         "isAuto": self.isAuto,
                         "reportType": self.reportType,
                         "apiKey": self.apiKey,
                         "supplierInn": self.supplierInn,
                         "customerInn": self.customerInn}
        if len(result_inputs['data']['data']['reportYears']) == 0:
            return {'status_code': 406, 'data': 'Client Error: the following parameters are not specified: pl2110_d1, pl2400_d1 (нет истории)'}
        if self.reportType == 'Q':
            response_data = result_inputs['data']['data']
            self.add_params(param_request=param_request, response_data=response_data)
        response = requests.post(self.ow_url + '/guarantee/score_guarantee',
                                 headers=self.headers,
                                 json=param_request)
        json_response = response.json()
        logger.info(f'get_score_guarantee response: {json_response}')
        response_data = self.create_response(json_response=json_response)
        logger.info(f'response_data: {response_data}')
        return {'status_code': response.status_code, 'data': response_data}

    def get(self, request, *args, **kwargs):
        if kwargs.get('report_type'):
            if kwargs['report_type'].upper() == 'Q':
                self.reportType = kwargs['report_type'].upper()
        result_score_guarantee = self.get_score_guarantee()
        return Response({'data': result_score_guarantee['data']})

    def update_base(self):
        result_score_guarantee = self.get_score_guarantee()
        if result_score_guarantee['status_code'] == 406:
            supplier = Principal.objects.filter(legal_entity__inn=self.supplierInn).first()
            customer = Beneficiary.objects.filter(legal_entity__inn=self.customerInn).first()
            score_guarantee = OliverWymanModel.objects.get_or_create(
                supplier=supplier,
                customer=customer,
                supplierInn=self.supplierInn,
                customerInn=self.customerInn,
                purchaseNumber=self.purchaseNumber,
                reportType=self.reportType)[0]
            return {'status_code': result_score_guarantee['status_code'], 'data': result_score_guarantee['data']}
        if result_score_guarantee['status_code'] != 200:
            return {'status_code': result_score_guarantee['status_code'], 'data': result_score_guarantee['data']}
        response_data = result_score_guarantee['data']

        supplier = Principal.objects.filter(legal_entity__inn=self.supplierInn).first()
        customer = Beneficiary.objects.filter(legal_entity__inn=self.customerInn).first()
        score_guarantee = OliverWymanModel.objects.get_or_create(
            supplier=supplier,
            customer=customer,
            supplierInn=self.supplierInn,
            customerInn=self.customerInn,
            purchaseNumber=self.purchaseNumber,
            reportType=self.reportType)[0]

        response_data_signals = response_data['signals']
        score_guarantee.signals_BS_1 = response_data_signals['BS_1'] != 'No'
        score_guarantee.signals_BS_2 = response_data_signals['BS_2'] != 'No'
        score_guarantee.signals_BS_5 = response_data_signals['BS_5'] != 'No'
        score_guarantee.signals_BS_6 = response_data_signals['BS_6'] != 'No'
        score_guarantee.signals_BS_7 = response_data_signals['BS_7'] != 'No'
        score_guarantee.signals_BS_10 = response_data_signals['BS_10'] != 'No'
        score_guarantee.signals_BS_14 = response_data_signals['BS_14'] != 'No'
        score_guarantee.signals_BS_15 = response_data_signals['BS_15'] != 'No'
        score_guarantee.signals_BS_16 = response_data_signals['BS_16'] != 'No'
        score_guarantee.signals_BS_18 = response_data_signals['BS_18'] != 'No'
        score_guarantee.signals_BS_22 = response_data_signals['BS_22'] != 'No'
        score_guarantee.signals_BS_23 = response_data_signals['BS_23'] != 'No'
        score_guarantee.signals_BS_111 = response_data_signals['BS_111'] != 'No'
        score_guarantee.signals_GS_0 = response_data_signals['GS_0'] != 'No'

        response_data_courts_factors = response_data['courts']
        score_guarantee.courts_1 = Decimal(
            response_data_courts_factors['Number of courts as a defendant during previous 2 year'])
        score_guarantee.courts_2 = Decimal(
            response_data_courts_factors['Average length of a court case during previous 2 years'])
        score_guarantee.courts_3 = Decimal(
            response_data_courts_factors['Number of courts as a claimer during previous 2 years'])
        score_guarantee.courts_4 = Decimal(
            response_data_courts_factors['Total case value of all courts during previous year as a defendant'])
        score_guarantee.courts_5 = Decimal(
            response_data_courts_factors[
                'Total case value of all courts during previous year as defendant / Net Profit'])
        score_guarantee.courts_6 = Decimal(
            response_data_courts_factors['Total case value of all courts during previous year as defendant / EBITDA'])

        response_data_executory_factors = response_data['executory']
        score_guarantee.executory_1 = Decimal(
            response_data_executory_factors['Number of sufficient enforcement proceeding cases for the last 2 years'])
        score_guarantee.executory_2 = Decimal(
            response_data_executory_factors['Total enforcement proceeding sum for the last year / Net Profit'])

        response_data_tenders_factors = response_data['tenders']
        score_guarantee.tenders_1 = Decimal(
            response_data_tenders_factors['Total number of tenders for the last year'])
        score_guarantee.tenders_2 = Decimal(
            response_data_tenders_factors['Tenders with the same Beneficiary that were won for the last 5 years'])
        score_guarantee.tenders_3 = Decimal(
            response_data_tenders_factors['Percentage of tenders won by the Principal for the last 2 years'])
        score_guarantee.tenders_4 = Decimal(
            response_data_tenders_factors['Total sum for tenders for the last year / Revenue'])

        response_data_score_data = response_data['score_data']
        score_guarantee.courts_module = Decimal(response_data_score_data['courts_module'])
        score_guarantee.executory_module = Decimal(response_data_score_data['executory_module'])
        score_guarantee.finance_module = Decimal(response_data_score_data['finance_module'])
        score_guarantee.pd_pit = Decimal(response_data_score_data['pd_pit'])
        score_guarantee.pd_ttc = Decimal(response_data_score_data['pd_ttc'])
        score_guarantee.qualitative_module = Decimal(response_data_score_data['qualitative_module'])
        score_guarantee.signals_module = Decimal(response_data_score_data['signals_module'])
        score_guarantee.tenders_module = Decimal(response_data_score_data['tenders_module'])

        response_data_finance = response_data['finance']
        score_guarantee.capital_assets = Decimal(response_data_finance['Capital / Assets'])
        score_guarantee.dynamics_of_revenue_year_to_year = \
            Decimal(response_data_finance['Dynamics of revenue (year-to-year)'])
        score_guarantee.EBITDA_short_term_debt_cash_and_interest_payments = \
            Decimal(response_data_finance['EBITDA / (Short-term debt - Cash and interest payments)'])
        score_guarantee.EBITDA_total_liabilities = Decimal(response_data_finance['EBITDA / Total liabilities'])
        score_guarantee.instant_liquidity = Decimal(response_data_finance['Instant liquidity'])
        score_guarantee.net_profit_cost_of_sales = Decimal(response_data_finance['Net profit / Cost of sales'])
        score_guarantee.revenues_current_assets = Decimal(response_data_finance['Revenues / Current Assets'])
        score_guarantee.total_liabilities_this_year_total_liabilities_previous_year = \
            Decimal(response_data_finance['Total liabilities (this year) / Total liabilities (previous year)'])

        score_guarantee.save()
        logger.info(f'score_guarantee done: supplierInn={self.supplierInn}, customerInn=self.customerInn')

        return {'data': response_data}

    def get_olyver_wyman_score_guarantee(self):
        logger.info(f'supplierInn: {self.supplierInn}, customerInn: {self.customerInn}')
        logger.info(f'ow_url: {self.ow_url}, ow_login: {self.ow_login}, ow_password: {self.ow_password}')
        if self.ow_url and self.ow_login and self.ow_password:
            return self.update_base()
        return {'error': _("there are no oliver_wyman's params in environment")}
