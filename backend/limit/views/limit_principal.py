import logging
import os
import re
from datetime import datetime
from dateparser import parse

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class LimitPrincipal(object):
    def __init__(self, inn, start_price, data_contracts=list(), fin_indicators=list(), info_principal=list()):
        self.url_data_contracts = os.getenv("KONTUR_URL_GOV_PURCHASES")
        self.url_fin_indicators = os.getenv("KONTUR_URL_BUH")
        self.url_info_principal = os.getenv("KONTUR_URL_DETAIL")
        self.kontur_key = os.getenv("KONTUR_KEY_TEST")
        self.inn = inn  # 6663003127
        self.data_contracts = data_contracts
        self.fin_indicators = fin_indicators
        self.info_principal = info_principal
        self.start_price_contract = start_price  # TODO подтягивать из модели Принципала
        self.SDP = 1.5  # СДП - Средняя дюрация портфеля
        self.PROCEDES = dict()  # Тут храним Выручка1 и Выручка2
        self.RATING = dict()
        self.financial_indicators = 0
        self.score_big_contracts = 0
        self.score_all_contracts = 0
        self.score_year = 0
        self.work_exp = 0
        self.fc = dict()
        self.fc_prev = dict()

    def get_kontur_data(self, url):
        try:
            response = requests.get(url, params={"inn": self.inn, "key": self.kontur_key})
            return response.json()
        except Exception as e:
            logging.error(e)
            return False

    # Этап 1
    def get_executed_contract_last_three_year(self, data_contracts):
        """Возвращает исполненные контракты за последние 3 года"""
        current_date = datetime.now()
        last_three_year = current_date.replace(year=current_date.year - 3)

        filter_data = []
        purchasesOfParticipant = data_contracts[0]["purchasesOfParticipant"]
        for el in purchasesOfParticipant:
            for k, v in el.items():
                if "contractExecutionDate" in k:
                    date = self.parce_date_kontur(v)
                    if date and date >= last_three_year:
                        filter_data.append(el)
        # Возвращает сразу фильтрованне данные:
        clen_contracts = self.get_filter_partially_executed(self.get_filter_execution_completed(filter_data))
        return clen_contracts

    def parce_date_kontur(self, date):
        """ Парсит дату по шаблону """
        patterns = [
            '\d{4}-\d{2}-\d{2}',    # noqa 2020-10-22 
            '\d{2}\.\d{2}\.\d{4}',  # noqa 22.10.2020
            '\d{4}\.\d{2}\.\d{2}',  # noqa 2020.10.22
            '\w*\s\d{4}',           # noqa январь 2020
        ]
        for pattern in patterns:
            date_search = re.findall(pattern, date)
            if len(date_search) != 0:
                date_search = date_search[-1]
            else:
                continue
            if patterns.index(pattern) == 0:
                return datetime.strptime(date_search, "%Y-%m-%d")
            if patterns.index(pattern) == 1:
                date_search = "-".join(date_search.split('.')[::-1])
                return datetime.strptime(date_search, "%Y-%m-%d")
            if patterns.index(pattern) == 2:
                date_search = date_search.replace(".", "-")
                return datetime.strptime(date_search, "%Y-%m-%d")
            if patterns.index(pattern) == 3:
                return parse(date_search)
        return None

    def get_filter_execution_completed(self, contracts):
        """Забирает только executionCompleted (вызывается в методе get_executed_contract)"""
        filter_data = []
        for el in contracts:
            for k, v in el.items():
                if "contractStage" in k and v == "executionСompleted":
                    filter_data.append(el)
        return filter_data

    def get_filter_partially_executed(self, contracts):
        """Забирает только partiallyExecuted (вызывается в методе get_executed_contract)"""
        filter_data = []
        for el in contracts:
            for k, v in el.items():
                if "partiallyExecuted" in k and v:
                    filter_data.append(el)
        return filter_data

    # Расчитваем СГК
    def get_sum_contract_last_three_year(self, data_contracts):
        """Возвращает среднюю сумму исполненные госконтрактов
        за последние три года
        """
        sum_contracts = 0
        for el in data_contracts:
            for k, v in el.items():
                if "contractPrice" in k:
                    sum_contracts += v["sum"]
        return sum_contracts / 3

    def get_fin_indicator(self, code, form):
        """Возвращает финансовый показатель по коду"""
        for el in self.fin_indicators[0]["buhForms"][-1][form]:
            for k, v in el.items():
                if k == "code":
                    if v == code:
                        return el["endValue"]
        return 0

    def get_proceeds(self, arr):
        """Возвращает выручку за текущий и предыдущий год."""
        for el in arr:
            for k, v in el.items():
                if k == "code":
                    if v == 2110:
                        return el["endValue"]

    def calculating_of_points(self):
        """Расчитывает финансовые индикаторы"""
        fc = dict()
        fc_prev = dict()
        codes_list = [
            (1100, "form1"),
            (1150, "form1"),
            (1200, "form1"),
            (1300, "form1"),
            (1370, "form1"),
            (1410, "form1"),
            (1500, "form1"),
            (1510, "form1"),
            (2110, "form2"),
            (2300, "form2"),
            (2320, "form2"),
            (2330, "form2"),
            (2400, "form2"),
        ]

        for code in codes_list:
            code_dist = self.get_fin_indicator(code[0], code[1])
            fc[f"{code[0]}"] = code_dist

        self.fc = fc
        code_dist = 0
        for el in self.fin_indicators[0]["buhForms"][-2]["form1"]:
            for k, v in el.items():
                if k == "code":
                    if v == 1300:
                        code_dist = el["endValue"]
        fc_prev["1300"] = code_dist
        self.fc_prev = fc_prev

        # Считаем выручку текущую и за предыдущий год
        current_2110 = self.fin_indicators[0]["buhForms"][-1]['form2']
        last_2110 = self.fin_indicators[0]["buhForms"][-2]['form2']

        self.PROCEDES['procedes_current'] = self.get_proceeds(current_2110)
        self.PROCEDES['procedes_last'] = self.get_proceeds(last_2110)

        depreciation = fc["1150"] * 0.08
        sos = (fc["1300"] - fc["1100"]) / fc["1200"] if fc["1200"] else 0
        fin_leverage = (fc["1410"] + fc["1510"]) / fc["1300"] if fc["1300"] else 0
        curr_liquid = 10 if fc["1200"] != 0 and fc["1500"] == 0 else fc["1200"] / fc["1500"]

        if (fc["2300"] + fc["2330"] + depreciation - fc["2320"]) > 0 and fc["2110"] == 0:
            ebitda = 10
        elif (fc["2300"] + fc["2330"] + depreciation - fc["2320"]) < 0 and fc["2110"] == 0:
            ebitda = 0
        else:
            ebitda = (fc["2300"] + fc["2330"] + depreciation - fc["2320"]) / fc["2110"]

        if (fc["2300"] + fc["2330"] + depreciation - fc["2320"]) == 0:
            debt_load = 0
        else:
            debt_load = (fc["1410"] + fc["1510"]) / (fc["2300"] + fc["2330"] + depreciation - fc["2320"])

        interest_service = (fc["2300"] + fc["2330"] + depreciation - fc["2320"]) / fc["2330"]
        annual_revenue_NCC = fc["2110"] / self.start_price_contract

        fin_indicator = {
            "sos": sos,
            "fin_leverage": fin_leverage,
            "curr_liquid": curr_liquid,
            "ebitda": ebitda,
            "debt_load": debt_load,
            "interest_service": interest_service,
            "annual_revenue_NCC": annual_revenue_NCC,
        }
        return fin_indicator

    def get_check_constuction(self):
        """Возвращает True если компания строительная(45)"""
        pa = self.info_principal[0]["UL"]["activities"]["principalActivity"]
        if "code" in pa:
            if re.search(r"^45", pa["code"]):
                return True
        return False

    # Расчитываем Фин стабильность (баллы)
    def calculating_financial_stability(self):
        """Расчитываем финансовую устойчивость принципала"""
        fin_indicator = self.calculating_of_points()
        construction = self.get_check_constuction()

        score = []
        if construction:
            score.append(self.get_score_sos_constructor(fin_indicator["sos"]))
        else:
            score.append(self.get_score_sos_not_constructor(fin_indicator["sos"]))
        score.append(self.get_score_fin_leverage(fin_indicator["fin_leverage"]))
        score.append(self.get_score_curr_liquid(fin_indicator["curr_liquid"]))
        score.append(self.get_score_ebitda(fin_indicator["ebitda"]))
        score.append(self.get_score_debt_load(fin_indicator["debt_load"]))
        score.append(self.get_score_interest_service(fin_indicator["interest_service"]))
        score.append(self.get_score_annual_revenue_NCC(fin_indicator["annual_revenue_NCC"]))

        return sum(score) * 0.5

    def get_score_sos_constructor(self, item):
        point = 0
        if item > 0:
            point += 10
        if item == 0:
            point += 3
        return round(point * 0.16, 3)

    def get_score_sos_not_constructor(self, item):
        point = 0
        if 0.5 < item:
            point += 10
        if 0.2 < item <= 0.5:
            point += 7
        if 0.1 < item <= 0.2:
            point += 5
        if 0 <= item <= 0.1:
            point += 3
        return round(point * 0.16, 3)

    def get_score_fin_leverage(self, item):
        point = 0
        if 0 <= item <= 1:
            point += 10
        if 1 < item <= 2:
            point += 7
        if 2 < item <= 3:
            point += 5
        if 3 < item <= 6:
            point += 3
        return round(point * 0.13, 3)

    def get_score_curr_liquid(self, item):
        point = 0
        if 2 < item:
            point += 10
        if 1.5 < item <= 2:
            point += 7
        if 1 < item <= 1.5:
            point += 5
        if 0.5 <= item <= 1:
            point += 3
        return round(point * 0.2, 3)

    def get_score_ebitda(self, item):
        point = 0
        if 20 < item:
            point += 10
        if 10 < item <= 20:
            point += 7
        if 5 < item <= 10:
            point += 5
        if 0 <= item <= 5:
            point += 3
        return round(point * 0.15, 3)

    def get_score_debt_load(self, item):
        point = 0
        if 0 <= item < 2:
            point += 10
        if 2 <= item < 3:
            point += 7
        if 3 <= item <= 6:
            point += 5
        return round(point * 0.17, 3)

    def get_score_interest_service(self, item):
        point = 0
        if 20 < item:
            point += 10
        if 5 < item <= 20:
            point += 7
        if 2.25 < item <= 5 or item == 0:
            point += 5
        if 1.1 < item <= 2.25:
            point += 3
        return round(point * 0.07, 3)

    def get_score_annual_revenue_NCC(self, item):
        point = 0
        if 3 < item:
            point += 10
        if 2 < item <= 3:
            point += 7
        if 1 < item <= 2:
            point += 5
        if 0.5 <= item <= 1:
            point += 3
        return point * 0.12

    # Расчитываем Опыт работы (баллы)
    def calculating_experience(self):
        """Расчитываем Опыт работы"""
        count = 0
        current_date = datetime.now()
        f_start_date = current_date.replace(year=current_date.year - 3)

        for el in self.data_contracts:
            for k, v in el.items():
                if "contractPrice" in k:
                    if v["sum"] >= self.start_price_contract:
                        count += 1

        # 3. Срок работы Принципала в основном направлении деятельности
        start_date = self.info_principal[0]["UL"]["activities"]["principalActivity"]["date"]
        f_start_date = datetime.strptime(start_date, "%Y-%m-%d")
        num_of_year = round((datetime.now() - f_start_date).days / 365)

        score_big = self.get_score_num_contract_big(count)
        score_all = self.get_score_num_contract_all(len(self.data_contracts))
        score_year = self.get_score_num_of_year(num_of_year)
        self.score_big_contracts = score_big
        self.score_all_contracts = score_all
        self.score_year = score_year
        self.work_exp = (score_big * 0.25 + score_all * 0.25 + score_year * 0.5) * 0.4
        return (score_big * 0.25 + score_all * 0.25 + score_year * 0.5) * 0.4

    def get_score_num_contract_big(self, item):
        """Возвращает баллы по кол-ву контрактов"""
        if item >= 3:
            return 10
        if item == 2:
            return 7
        if item == 1:
            return 5
        if item == 0:
            return 0

    def get_score_num_contract_all(self, item):
        """Возвращает кол-во баллов исходя оценки кол-ва исполненных контрактов"""
        if item >= 5:
            return 10
        if 3 <= item <= 4:
            return 7
        if item == 2:
            return 5
        if item == 1:
            return 3
        if item == 0:
            return 0

    def get_score_num_of_year(self, item):
        """Возвращает кол-во баллов исходя из кол-ва лет в этой сфере"""
        if item > 3:
            return 10
        if 1 <= item <= 3:
            return 5
        if item < 1:
            return 0

    # Этап 2
    def get_factor_1(self):
        """Наличие существенной по суммам и/или срокам текущей Картотеки неопл. расчетов"""
        return False

    def get_factor_2(self):
        """Наличие существенной по суммам и/или срокам задолженности перед фед. бюдж."""
        return False

    def get_factor_3(self):
        """Наличие просроченной задолженности перед работниками по зараб. плате"""
        return False

    def get_factor_4(self):
        """Бюджетные активы, неликвидные запасы на последнюю отчетную дату"""
        return False

    def get_factor_5(self):
        """Безнадежная дебиторская задолженность на последнюю отчетную дату"""
        return False

    def get_factor_6(self):
        """Наличие текущего убытка с учетом что имеется накопленная прибыль"""
        if len(self.fc) == 0:
            return False
        if self.fc['2400'] > 0:
            return False
        if self.fc_prev['1300'] != 0:
            if (self.fc['1300'] / self.fc_prev['1300'] - 1) < -0.25 and self.fc['1370'] > 0:
                return True
        return False

    def get_factor_7(self):
        """Текущий убыток при условии что ЧА положительные"""
        if len(self.fc) == 0:
            return False
        if self.fc['2400'] > 0:
            return False
        if self.fc_prev['1300'] != 0:
            if (self.fc['1300'] / self.fc_prev['1300'] - 1) >= -0.25:
                return True
        return False

    def get_factor_8(self):
        """Существенное снижение ЧА"""
        if len(self.fc) == 0:
            return False
        if self.fc_prev['1300'] != 0:
            if (self.fc['1300'] / self.fc_prev['1300'] - 1) >= -0.25 and self.fc['1370'] > 0 and self.fc['2400'] > 0:
                return True
        return False

    def get_factor_9(self):
        """Участие в судебном(ых) процессе(ах)"""
        return False

    def additional_factors(self):
        """Считаем доп факторы"""
        factors = {
            "factor_1": self.get_factor_1(),
            "factor_2": self.get_factor_2(),
            "factor_3": self.get_factor_3(),
            "factor_4": self.get_factor_4(),
            "factor_5": self.get_factor_5(),
            "factor_6": self.get_factor_6(),
            "factor_7": self.get_factor_7(),
            "factor_8": self.get_factor_8(),
            "factor_9": self.get_factor_9(),
        }
        # score = sum(0.11 for v in factors.values() if v)
        score = sum(1 for v in factors.values() if v)
        return {'score': score, 'factors': factors}

    # Этап 3
    def get_principal_rating(self, total):
        rating_list = {
            9.3: ("A+", 4.5, 50),
            8.6: ("A", 4.0, 50),
            7.9: ("A-", 3.5, 50),
            7.2: ("B+", 3.0, 35),
            6.5: ("B", 2.5, 35),
            5.8: ("B-", 2.0, 35),
            5.1: ("C+", 1.5, 20),
            4.4: ("C", 1.0, 20),
            3.5: ("C-", 0, 0),
            0: ("D", 0, 0),
        }
        for max_n, data in rating_list.items():
            if total >= max_n:
                self.RATING = {"rating": data[0], "k": data[1], "mdo": data[2]}
                return self.RATING

    def limit_principal_1(self):
        """Возвращает литмит принципала расчитанный по формуле
        Lp = СГК * k * МДО
        """
        fin_big = self.calculating_financial_stability()
        exper = self.calculating_experience()
        additional_factors = self.additional_factors()
        total_score = fin_big + exper
        rating = self.get_principal_rating(total_score)
        sgk = self.get_sum_contract_last_three_year(self.data_contracts)
        ball_rating_total = min(total_score - additional_factors['score'] * 0.11, 9.9)
        letter_rating = self.get_principal_rating(ball_rating_total)['rating']
        data_principal = {
            "limit": sgk * rating["k"] * rating["mdo"],
            "ball_rating": total_score,
            "letter_rating": letter_rating,
            "financial_indicators": fin_big,
            "score_big_contracts": self.score_big_contracts,
            "score_all_contracts": self.score_all_contracts,
            "score_year": self.score_year,
            "work_exp": self.work_exp,
            "additional_factors": additional_factors['score'],
            "factors": additional_factors['factors'],
            "ball_rating_total": ball_rating_total,
        }
        return data_principal

    def limit_principal_2(self, avg_procedes=0):
        """Возвращает литмит принципала расчитанный по формуле
        Lp = ((Выручка1 + Выручка2)/2) * 0,25 * k * МДО * СДП
        """
        avg_procedes = 0
        if self.PROCEDES:
            avg_procedes = (self.PROCEDES["procedes_current"] + self.PROCEDES["procedes_last"]) / 2
        limit = avg_procedes * 0.25 * self.RATING["k"] * self.RATING["mdo"] * self.SDP
        return round(limit, 3)

    def get_filter_data(self):
        all_contracts = self.get_kontur_data(self.url_data_contracts)
        self.data_contracts = self.get_executed_contract_last_three_year(all_contracts)
        self.fin_indicators = self.get_kontur_data(self.url_fin_indicators)
        self.info_principal = self.get_kontur_data(self.url_info_principal)

    def get_limit_principal(self):
        """Возвращает больший лимит принципала"""
        if not self.data_contracts and not self.fin_indicators and not self.info_principal:
            self.get_filter_data()

        limit = self.limit_principal_1()
        limit_2 = self.limit_principal_2()

        if limit["limit"] > limit_2:
            return limit
        limit["limit"] = limit_2
        return limit
