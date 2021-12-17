import os
import requests
from django.utils.translation import gettext as _

from ..models import AccountingFormDetail, AccountingForm  # noqa
from entity.models import Principal


class Kontur(object):
    def __init__(self, kontur_key=os.getenv('KONTUR_KEY'), kontur_url=os.getenv('KONTUR_URL')):
        self.kontur_key = kontur_key
        self.kontur_url = kontur_url

    def get_kontur_financial_indicators(self, inn):
        if self.kontur_url and self.kontur_key:
            return self.update_base(inn)
        return {'error': _(' no kontur_key or kontur_url in environment')}

    def update_base(self, inn):
        try:
            response = requests.get(self.kontur_url,
                                    params={
                                        "inn": inn,
                                        "key": self.kontur_key,
                                    })
            json_response = response.json()
            buh_forms = json_response[0]['buhForms']
            principal = Principal.objects.filter(legal_entity__inn=inn).first()

            if principal:

                for item in buh_forms:
                    year = item['year']
                    organization_type = item['organizationType']
                    accounting_form = AccountingForm.objects.get_or_create(
                        year=year,
                        organization_type=organization_type,
                        principal=principal,
                    )[0]

                    for key, value in item.items():
                        if 'form' in key:
                            for params in value:
                                accounting_form_detail = AccountingFormDetail.objects.get_or_create(  # noqa
                                    code=params['code'] if 'code' in params.keys() else None,
                                    line_name=params['name'] if 'name' in params.keys() else None,
                                    start_value=params['startValue'] if 'startValue' in params.keys() else 0,
                                    end_value=params['endValue'] if 'endValue' in params.keys() else 0,
                                    accounting_form=accounting_form
                                )

                    depreciation = \
                        AccountingFormDetail.objects.get_or_create(code='1150', accounting_form=accounting_form)[
                            0].end_value
                    depreciation = depreciation if depreciation else 0 * 0.08
                    contract_sum = 0
                    detail_1100 = \
                        AccountingFormDetail.objects.get_or_create(code='1100', accounting_form=accounting_form)[
                            0].end_value
                    detail_1100 = detail_1100 if detail_1100 else 0
                    detail_1200 = \
                        AccountingFormDetail.objects.get_or_create(code='1200', accounting_form=accounting_form)[
                            0].end_value
                    detail_1200 = detail_1200 if detail_1200 else 0
                    detail_1300 = \
                        AccountingFormDetail.objects.get_or_create(code='1300', accounting_form=accounting_form)[
                            0].end_value
                    detail_1300 = detail_1300 if detail_1300 else 0
                    detail_1410 = \
                        AccountingFormDetail.objects.get_or_create(code='1410', accounting_form=accounting_form)[
                            0].end_value
                    detail_1410 = detail_1410 if detail_1410 else 0
                    detail_1500 = \
                        AccountingFormDetail.objects.get_or_create(code='1500', accounting_form=accounting_form)[
                            0].end_value
                    detail_1500 = detail_1500 if detail_1500 else 0
                    detail_1510 = \
                        AccountingFormDetail.objects.get_or_create(code='1510', accounting_form=accounting_form)[
                            0].end_value
                    detail_1510 = detail_1510 if detail_1510 else 0
                    detail_2110 = \
                        AccountingFormDetail.objects.get_or_create(code='2110', accounting_form=accounting_form)[
                            0].end_value
                    detail_2110 = detail_2110 if detail_2110 else 0
                    detail_2300 = \
                        AccountingFormDetail.objects.get_or_create(code='2300', accounting_form=accounting_form)[
                            0].end_value
                    detail_2300 = detail_2300 if detail_2300 else 0
                    detail_2320 = \
                        AccountingFormDetail.objects.get_or_create(code='2320', accounting_form=accounting_form)[
                            0].end_value
                    detail_2320 = detail_2320 if detail_2320 else 0
                    detail_2330 = \
                        AccountingFormDetail.objects.get_or_create(code='2330', accounting_form=accounting_form)[
                            0].end_value
                    detail_2330 = detail_2330 if detail_2330 else 0
                    ebitda = (detail_2300 + detail_2330 + depreciation - detail_2320)

                    security_of_current_assets = (detail_1300 - detail_1100) / detail_1200 if detail_1200 != 0 else 0
                    financial_leverage = (detail_1410 + detail_1510) / detail_1300 if detail_1300 != 0 else 0
                    current_liquidity = detail_1200 / detail_1500 if detail_1500 != 0 else 0
                    profitability_ebitda = ebitda / detail_2110 if detail_2110 != 0 else 0
                    debt_burden = (detail_1410 - detail_1510) / ebitda if ebitda != 0 else 0
                    interest_service = ebitda / detail_2330 if detail_2330 != 0 else 0
                    annual_revenue_to_ncc = detail_2110 / contract_sum if contract_sum != 0 else 0

                    security_of_current_assets = AccountingFormDetail.objects.get_or_create(
                        code='security_of_current_assets', line_name='Обеспеченность текущих активов СОС',
                        end_value=security_of_current_assets, accounting_form=accounting_form)
                    financial_leverage = AccountingFormDetail.objects.get_or_create(
                        code='financial_leverage', line_name='Финансовый леверидж', end_value=financial_leverage,
                        accounting_form=accounting_form)
                    current_liquidity = AccountingFormDetail.objects.get_or_create(
                        code='current_liquidity', line_name='Текущая ликвидность', end_value=current_liquidity,
                        accounting_form=accounting_form)
                    profitability_ebitda = AccountingFormDetail.objects.get_or_create(
                        code='profitability_ebitda', line_name='Рентабельность ebitda', end_value=profitability_ebitda,
                        accounting_form=accounting_form)
                    debt_burden = AccountingFormDetail.objects.get_or_create(
                        code='debt_burden', line_name='Долговая нагрузка (долг/ebitda)', end_value=debt_burden,
                        accounting_form=accounting_form)
                    interest_service = AccountingFormDetail.objects.get_or_create(
                        code='interest_service', line_name='Обслуживание процентов (ebitda/%)',
                        end_value=interest_service, accounting_form=accounting_form)
                    annual_revenue_to_ncc = AccountingFormDetail.objects.get_or_create(
                        code='annual_revenue_to_ncc', line_name='Годовая выручка к НЦК',
                        end_value=annual_revenue_to_ncc, accounting_form=accounting_form)

            return response.json()
        except Exception as err:
            print(err)
        return {}
