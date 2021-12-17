from datetime import datetime
import logging
import os
import requests

from rest_framework.response import Response

from ..models import Order, Factors, OrderFactors
from handbook.models import BlackListItem

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class GetFactors(object):
    def __init__(self, init_params):
        if 'order' in init_params:
            self.order_id = init_params['order']
            self.order = Order.objects.filter(pk=self.order_id).first()
            self.principal = self.order.principal
            self.beneficiary = self.order.beneficiary
            self.principal_inn = self.principal.legal_entity.inn
            self.beneficiary_inn = self.beneficiary.legal_entity.inn
        else:
            self.order = None
        self.url_req = os.getenv("KONTUR_URL_REQ")
        self.kontur_key = os.getenv("KONTUR_KEY")
        self.purchases_data = list()
        self.buh_data = list()
        self.detail_data = list()
        self.req_data = list()
        self.blocking_acc = list()
        self.check_pass_data = list()
        self.analytics_data = list()
        self.person_bankruptcy_data = list()
        self.fssp_data = list()
        self.petitioners_of_arbitration_data = list()
        self.selection_by_reg_date_data = list()
        self.beneficial_owners_data = list()

        self.inn = self.principal_inn

    def get_factor(self, type, catalog):
        factor = Factors.objects.get_or_create(type=type, catalog=catalog)[0]
        factor.title = type
        factor.save()
        return factor

    def update_factor(self, type, catalog, value):
        factor = self.get_factor(type=type, catalog=catalog)
        if factor.value:
            item = OrderFactors.objects.get_or_create(order=self.order, factors=factor)[0]
            item.value = value
            item.save()

    def get_black_list_item(self, inn):
        item = BlackListItem.objects.get_or_create(inn=inn)
        item.save()
        return item

    def update_black_list_item(self, inn, title=None, comment=None):
        item = self.get_black_list_item(inn)
        item.title = title
        item.save()

    def _get_region_city_fullname(self, inn) -> tuple:
        response = requests.get(os.getenv("KONTUR_URL_REQ"),
                                params={"inn": inn, "key": self.kontur_key})
        response.json()
        try:
            region_name = response.json()[0]['UL']['legalAddress']['parsedAddressRF']['regionName']['topoValue']
            topo_full_name = response.json()[0]['UL']['legalAddress']['parsedAddressRF']['regionName']['topoFullName']
            city_name = response.json()[0]['UL']['legalAddress']['parsedAddressRF']['city']['topoValue']
            city_full_name = f"{response.json()[0]['UL']['legalAddress']['parsedAddressRF']['city']['topoFullName']} {city_name}"  # noqa
        except Exception as ex:
            logging.error(ex)
            return None, None
        region_full_name = f'{region_name} {topo_full_name}'
        return region_full_name, city_full_name

    def get_kontur_data(self, url):
        try:
            response = requests.get(url, params={"inn": self.inn, "key": self.kontur_key})
            return response.json()
        except Exception as e:
            logging.error(e)
            return False

    def get_purchases(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_PURCHASES"))
        except Exception as e:
            logging.error(e)
            return Response({"errreq_dataor": "no data on the principal with the given inn"}, status=400)
        self.purchases_data = kontur_data

    def get_req_data(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_REQ"))
        except Exception as e:
            logging.error(e)
            return Response({"errreq_dataor": "no data on the principal with the given inn"}, status=400)
        self.req_data = kontur_data

    def get_detail(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_DETAIL"))
        except Exception as e:
            logging.error(e)
            return Response({"errreq_dataor": "no data on the principal with the given inn"}, status=400)
        self.detail_data = kontur_data

    def get_buh(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_BUH"))
        except Exception as e:
            logging.error(e)
            return Response({"errreq_dataor": "no data on the principal with the given inn"}, status=400)
        self.buh_data = kontur_data

    def get_blocking_acc(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_BLOCKING_BANK_ACCOUNTS"))
        except Exception as e:
            logging.error(e)
            return Response({"error": "no data on the principal with the given inn"}, status=400)
        self.blocking_acc = kontur_data

    def get_check_pass(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_CHECK_PASSPORT"))
        except Exception as e:
            logging.error(e)
            return Response({"error": "no data on the principal with the given inn"}, status=400)
        self.check_pass_data = kontur_data

    def get_analytics(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_ANALYTICS"))
        except Exception as e:
            logging.error(e)
            return Response({"error": "no data on the principal with the given inn"}, status=400)
        self.analytics_data = kontur_data

    def get_person_bankruptcy(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_PERSON_BANKRUPTCY"))
        except Exception as e:
            logging.error(e)
            return Response({"error": "no data on the principal with the given inn"}, status=400)
        self.person_bankruptcy_data = kontur_data

    def get_sanctioned_persons(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_SANCTIODEN_PERSONS"))
        except Exception as e:
            logging.error(e)
            return Response({"error": "no data on the principal with the given inn"}, status=400)
        self.sanctioned_persons_data = kontur_data

    def get_fssp(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_FSSP"))
        except Exception as e:
            logging.error(e)
            return Response({"error": "no data on the principal with the given inn"}, status=400)
        self.fssp_data = kontur_data

    def get_petitioners_of_arbitration(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_PETITIONERS_OF_ARBITRATION"))
        except Exception as e:
            logging.error(e)
            return Response({"error": "no data on the principal with the given inn"}, status=400)
        self.petitioners_of_arbitration_data = kontur_data

    def get_selection_by_reg_date(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_SELECTION_BY_REG_DATE"))
        except Exception as e:
            logging.error(e)
            return Response({"error": "no data on the principal with the given inn"}, status=400)
        self.selection_by_reg_date_data = kontur_data

    def get_beneficial_owners(self):
        try:
            kontur_data = self.get_kontur_data(url=os.getenv("KONTUR_URL_BENEFICIAL_OWNERS"))
        except Exception as e:
            logging.error(e)
            return Response({"error": "no data on the principal with the given inn"}, status=400)
        self.beneficial_owners_data = kontur_data

    def get_PERIOD_OF_ACTIVITY(self):
        try:
            registrationDate = self.req_data[0]['UL']['registrationDate']
            registrationDate_dt = datetime.strptime(registrationDate, '%Y-%m-%d')
            period = (datetime.now() - registrationDate_dt).days
        except Exception as ex:
            logging.error(ex)
            return False
        guaranty_sum = 0
        sum = 0
        if sum >= 35000000.00 and guaranty_sum >= 10000000.01:
            return not period >= 360
        if sum >= 10000000.00 and guaranty_sum >= 1000000.01:
            return not period >= 270
        if sum >= 1000000.00 and guaranty_sum >= 500000.01:
            return not period >= 180
        if guaranty_sum < 500000.01:
            return not period >= 90
        return False

    def get_USRoLE_REGISTRATION(self):
        try:
            statusString = self.req_data[0]['UL']['status']['statusString']
        except Exception as ex:
            logging.error(ex)
            return False
        return statusString != 'Действующее'

    def get_LIQUIDATION_BANKRUPTCY(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if 'm7037' in data:
            return data['m7037']
        return False

    def liquidation_bankruptcy_participant(self):
        try:
            bankrupting = self.req_data[0]['status']['bankrupting']
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if 'm7037' in data:
            return data['m7037']
        if bankrupting:
            return True
        return False

    def get_LIQUIDATION_BANKRUPTCY_STATEMENT(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if 'm8001' in data:
            return data['m7015']
        return False

    def get_LIST_OF_TERRORISTS_EXTREMISTS(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        codes = list()
        codes.append('m8001')
        codes.append('m8002')
        codes.append('m8003')
        codes.append('m8004')
        codes.append('m8005')
        codes.append('m8006')
        codes.append('m8007')
        codes.append('m8008')
        codes.append('m8009')
        codes.append('m8010')
        codes.append('m8011')
        codes.append('m8012')
        for code in codes:
            if code in data:
                return True
        return False

    def get_UNRELIABLE_INFO_IN_THE_USRoLE(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if 'm8001' in data:
            return True
        return False

    def get_MASS_REGISTRATION(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if 'q7007' in data and data['q7007'] > 0:
            return True
        if 'q7009' in data and data['q7009'] > 0:
            return True
        if 'm5003' in data:
            return True
        return False

    def enforcement_proceedings(self):
        try:
            data = self.fssp_data
        except Exception as ex:
            logging.error(ex)
            return False
        for item in data:
            try:
                startDate = datetime.strptime(item['fssp']['startDate'], '%Y-%m-%d')
            except Exception as ex:
                logging.error(ex)
                return False
            offset = datetime.now() - startDate
            if offset.days >= 365:
                if item['inn'] == self.principal_inn and item['fssp']['sum'] <= 0.25:
                    return True
        return False

    def get_MASS_LEADER(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if data:
            if 'm5009' in data:
                return True
            if 'm5010' in data:
                return True
        return False

    def get_RNP(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if 'm4001' in data:
            return True
        return False

    def get_DISQUALIFIED_PERSONS(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if 'm5008' in data:
            return True
        if 'm5001' in data:
            return True
        return False

    def get_NO_ANNUAL_BO(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if 'm6002' in data:
            return not data['m6002']
        return False

    def get_USRoLE_REORGANIZATION(self):
        try:
            dissolving = self.req_data[0]['UL']['status']['dissolving']
            dissolved = self.req_data[0]['UL']['status']['dissolved']
            statusString = self.req_data[0]['UL']['status']['statusString']
            reorganizing = self.req_data[0]['UL']['status']['reorganizing']
            # analytics
            analytics = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        if 'm7042' in analytics:
            return analytics['m7042']
        if statusString != 'Действующее':
            return True
        if dissolved and dissolving:
            return True
        if reorganizing:
            return True
        return False

    def get_BLOCKING_ACCOUNTS(self):
        try:
            blocking_acc = self.blocking_acc[0]['blockedAccountsInfo']['totalCount']
        except Exception as ex:
            logging.error(ex)
            return False
        return blocking_acc > 0

    def get_SHAREHOLDER_VALIDITY_OF_PASSPORT(self):
        # return len(self.check_pass) != 0req
        return False

    def territory_at_risk(self):
        risk_territory = ['Республика Адыгея', 'Качаево-Черкесская Республика',
                          'Кабардино-Балкарская Республика', 'Республика Северная Осетия – Алания',
                          'Республика Ингушетия', 'Чеченская Республика', 'Республика Дагеста',
                          'Республика Крым', 'Город федерального значения Севастополь']
        try:
            region_name = self.req_data[0]['UL']['legalAddress']['parsedAddressRF']['regionName']['topoValue']
            topo_full_name = self.req_data[0]['UL']['legalAddress']['parsedAddressRF']['regionName']['topoFullName']
            city_name = self.req_data[0]['UL']['legalAddress']['parsedAddressRF']['city']['topoValue']
            city_full_name = f"{self.req_data[0]['UL']['legalAddress']['parsedAddressRF']['city']['topoFullName']} {city_name}"  # noqa
        except Exception as ex:
            logging.error(ex)
            return False
        region_full_name = f'{region_name} {topo_full_name}'
        if region_full_name in risk_territory:
            return True
        if city_full_name in risk_territory:
            return True
        return False

    def age_eio_ip(self):
        now = datetime.now()
        try:
            person = self.principal.legal_entity.fl
            person_birth_date = person.birth_date
            date_delta = now.date() - person_birth_date
        except Exception as ex:
            logging.error(ex)
            return False
        person_year_old = date_delta / 365.25
        str_person_year_old = str(person_year_old)[:2]
        if 22 <= float(str_person_year_old) <= 65:
            return False
        return True

    def cha(self):
        try:
            buh_forms = self.buh_data[0]['buhForms']
        except Exception as ex:
            logging.error(ex)
            return False
        for item in buh_forms:
            for key, value in item.items():
                if 'form' in key:
                    for params in value:
                        code = params['code'] if 'code' in params.keys() else None
                        start_value = params['startValue'] if 'startValue' in params.keys() else None
                        end_value = params['endValue'] if 'endValue' in params.keys() else None
                        if code == '1300' and end_value > start_value:
                            return False
                        if code == '1310' and end_value > start_value:
                            return False
        return True

    def negative_cha(self):
        try:
            buh_forms = self.buh_data[0]['buhForms']
        except Exception as ex:
            logging.error(ex)
            return False
        for item in buh_forms:
            for key, value in item.items():
                if 'form' in key:
                    for params in value:
                        code = params['code'] if 'code' in params.keys() else None
                        end_value = params['endValue'] if 'endValue' in params.keys() else None
                        if code == '1300' and end_value > 0:
                            return False
        return True

    def losses(self):
        try:
            buh_forms = self.buh_data[0]['buhForms']
        except Exception as ex:
            logging.error(ex)
            return False
        for item in buh_forms:
            for key, value in item.items():
                if 'form' in key:
                    for params in value:
                        code = params['code'] if 'code' in params.keys() else None
                        start_value = params['startValue'] if 'startValue' in params.keys() else None
                        end_value = params['endValue'] if 'endValue' in params.keys() else None
                        if code == '1370' and end_value < start_value:
                            return False
        return True

    def non_compliance_contract_with_revenue(self):  # noqa
        try:
            buh_forms = self.buh_data[0]['buhForms']
        except Exception as ex:
            logging.error(ex)
            return False
        for item in buh_forms:
            for key, value in item.items():
                if 'form' in key:
                    for params in value:
                        code = params['code'] if 'code' in params.keys() else None
                        start_value = params['startValue'] if 'startValue' in params.keys() else None
                        end_value = params['endValue'] if 'endValue' in params.keys() else None
                        if start_value and end_value:
                            try:
                                change_percent = abs(((float(end_value) - start_value) / end_value) * 100)
                                if code == '2110' and change_percent >= 20:
                                    return False
                            except ZeroDivisionError:
                                pass
        return True

    def compare_regions_principal_beneficiary(self):
        beneficiary = self._get_region_city_fullname(inn=self.beneficiary_inn)
        principal = self._get_region_city_fullname(inn=self.principal_inn)
        if beneficiary[0] == principal[0]:
            return True
        return False

    def unified_state_register_legal_entities_invalid(self):
        try:
            status = self.req_data[0]['UL']['status']['dissolved']
        except Exception as ex:
            logging.error(ex)
            return False
        if status:
            return True
        else:
            return False

    def activity_type(self):
        try:
            principal_activity_code = self.detail_data[0]['UL']['activities']['principalActivity']['code']
        except Exception as ex:
            logging.error(ex)
            return False
        unsuitable_OKVED = ['64', '66', '70']
        if str(principal_activity_code) in unsuitable_OKVED:
            return True
        return False

    def arbitration_stop(self):
        try:
            petitioners = self.petitioners_of_arbitration_data[0]['petitioners']
        except Exception as ex:
            logging.error(ex)
            return False
        for petitioner in petitioners:
            if petitioner['inn'] == self.principal_inn:
                return True
        return False

    def territory_at_risk_beneficiary(self):
        risk_territory = ['Республика Адыгея', 'Качаево-Черкесская Республика',
                          'Кабардино-Балкарская Республика', 'Республика Северная Осетия – Алания',
                          'Республика Ингушетия', 'Чеченская Республика', 'Республика Дагестан',
                          'Республика Крым', 'Город федерального значения Севастополь']
        reg, city = self._get_region_city_fullname(self.beneficiary_inn)
        if reg in risk_territory:
            return True
        if city in risk_territory:
            return True
        return False

    def frequent_change_tax_authority(self):
        date_list = []
        diff_list = []
        try:
            egr_records = self.detail_data[0]['UL']['egrRecords']
        except Exception as ex:
            logging.error(ex)
            return False
        for egr_record in egr_records:
            date_list.append(datetime.strptime(egr_record['date'], "%Y-%m-%d"))
        for first_date, second_date in zip(date_list[0::], date_list[1::]):
            diff_list.append(second_date - first_date)
        for date in diff_list:
            date_days_int = abs(date.days)
            if date_days_int < 365:
                return True
        return False

    def black_list(self):
        if BlackListItem.objects.filter(inn=self.principal_inn).exists():
            return True
        return False

    def revenue_decline(self):
        try:
            buh_forms = self.buh_data[0]['buhForms']
        except Exception as ex:
            logging.error(ex)
            return False
        for item in buh_forms:
            for key, value in item.items():
                if 'form' in key:
                    for params in value:
                        code = params['code'] if 'code' in params.keys() else None
                        start_value = params['startValue'] if 'startValue' in params.keys() else None
                        end_value = params['endValue'] if 'endValue' in params.keys() else None
                        if start_value and end_value:
                            result = end_value / start_value
                            if code == '2110' and abs(result) <= 0.5:
                                return True
        return False

    def dz_kz_growth(self):  # noqa
        try:
            buh_forms = self.buh_data[0]['buhForms']
        except Exception as ex:
            logging.error(ex)
            return False
        for item in buh_forms:
            for key, value in item.items():
                if 'form' in key:
                    for params in value:
                        code = params['code'] if 'code' in params.keys() else None
                        start_value = params['startValue'] if 'startValue' in params.keys() else None
                        end_value = params['endValue'] if 'endValue' in params.keys() else None
                        if start_value and end_value:
                            result = end_value / start_value
                            if code == '1230' and abs(result) <= 0.25:
                                return True
                        elif start_value and end_value:
                            result = end_value / start_value
                            if code == '1520' and abs(result) <= 0.25:
                                return True
        return False

    def arbitration_forced(self):
        try:
            data = self.analytics_data[0]['analytics']
        except Exception as ex:
            logging.error(ex)
            return False
        try:
            if not isinstance(data['s2014'] or data['s2025'], (type(None), type(''))):
                return True
        except KeyError as ex:
            logging.error(ex)
            return False
        return False

    def update_factors(self):
        catalog = 'STOP'
        self.update_factor(type='Срок деятельности', catalog=catalog, value=self.get_PERIOD_OF_ACTIVITY())
        self.update_factor(type='ЕГРЮЛ / Регистрация', catalog=catalog, value=self.get_USRoLE_REGISTRATION())
        self.update_factor(type='ЕГРЮЛ / Реорганизация', catalog=catalog, value=self.get_USRoLE_REORGANIZATION())
        self.update_factor(type='ЕГРЮЛ / Недействующее', catalog=catalog,
                           value=self.unified_state_register_legal_entities_invalid())
        # self.update_factor(type='ЕГРЮЛ / Уникальность', catalog=catalog, value=True)
        # self.update_factor(type='Приостановка деятельности', catalog=catalog, value=True)
        self.update_factor(type='Ликвидация / Банкротство', catalog=catalog, value=self.get_LIQUIDATION_BANKRUPTCY())
        self.update_factor(type='Ликвидация / Банкротство участников', catalog=catalog,
                           value=self.liquidation_bankruptcy_participant())
        self.update_factor(type='Список "массовых" руководителей, учредителей', catalog=catalog,
                           value=self.get_MASS_LEADER())
        self.update_factor(type='Блокировка счетов', catalog=catalog, value=self.get_BLOCKING_ACCOUNTS())
        self.update_factor(type='РНП', catalog=catalog, value=self.get_RNP())
        self.update_factor(type='Дисквалифицированные лица', catalog=catalog, value=self.get_DISQUALIFIED_PERSONS())
        self.update_factor(type='Отсутствие годовой БО', catalog=catalog, value=self.get_NO_ANNUAL_BO())
        self.update_factor(type='Территория с риском', catalog=catalog, value=self.territory_at_risk())
        self.update_factor(type='Территория с риском Бенефициар', catalog=catalog,
                           value=self.territory_at_risk_beneficiary())
        self.update_factor(type='Возраст ЕИО / ИП', catalog=catalog, value=self.age_eio_ip())
        self.update_factor(type='ЧА', catalog=catalog, value=self.cha())
        self.update_factor(type='Отрицательные ЧА', catalog=catalog, value=self.negative_cha())
        self.update_factor(type='Вид деятельности', catalog=catalog, value=self.activity_type())
        self.update_factor(type='Снижение выручки', catalog=catalog, value=self.revenue_decline())
        self.update_factor(type='Частая смена налогового органа', catalog=catalog,
                           value=self.frequent_change_tax_authority())
        self.update_factor(type='Черный список', catalog=catalog, value=self.black_list())
        self.update_factor(type='Арбитражи', catalog=catalog, value=self.arbitration_stop())

        catalog = 'FORCED'
        self.update_factor(type='Заявление о намерении', catalog=catalog,
                           value=self.get_LIQUIDATION_BANKRUPTCY_STATEMENT())
        self.update_factor(type='Список террористов/экстремистов', catalog=catalog,
                           value=self.get_LIST_OF_TERRORISTS_EXTREMISTS())
        self.update_factor(type='Список с оружием', catalog=catalog, value=self.get_LIST_OF_TERRORISTS_EXTREMISTS())
        self.update_factor(type='Недостоверная инфо в ЕГРЮЛ', catalog=catalog,
                           value=self.get_UNRELIABLE_INFO_IN_THE_USRoLE())
        self.update_factor(type='Массовая регистрация', catalog=catalog, value=self.get_MASS_REGISTRATION())
        self.update_factor(type='Исполнительные производства', catalog=catalog, value=self.enforcement_proceedings())
        self.update_factor(type='Убытки', catalog=catalog, value=self.losses())
        self.update_factor(type='Рост ДЗ/КЗ', catalog=catalog, value=self.dz_kz_growth())
        self.update_factor(type='Несоответствие контракта выручке', catalog=catalog,
                           value=self.non_compliance_contract_with_revenue())
        self.update_factor(type='Регионы', catalog=catalog, value=self.compare_regions_principal_beneficiary())
        self.update_factor(type='Арбитражи', catalog=catalog, value=self.arbitration_forced())
        catalog = 'PASSPORT_PRODUCT'
        # self.update_factor(type='Акционер Действительность паспортов', catalog=catalog,
        #                    value=self.get_SHAREHOLDER_VALIDITY_OF_PASSPORT())
        # self.update_factor(type='Задолженность по ЗП', catalog=catalog, value=False)
        # self.update_factor(type='Акционер Действительность паспортов', catalog=catalog, value=True)

    def update_base(self):
        logger.info(f'order: {self.order}')
        self.get_purchases()
        self.get_buh()
        self.get_req_data()
        self.get_detail()
        self.get_blocking_acc()
        self.get_check_pass()
        self.get_analytics()
        self.get_person_bankruptcy()
        self.get_fssp()
        self.get_petitioners_of_arbitration()
        self.get_selection_by_reg_date()
        self.get_beneficial_owners()

        self.update_factors()
