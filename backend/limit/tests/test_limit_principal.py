import json
import os

from app.basedir import BASE_DIR
from django.test import TestCase
from limit.views.limit_principal import LimitPrincipal


class LimitPrincipalTestCase(TestCase):
    def setUp(self):
        self.inn = 6663003127
        self.start_ammount = 200000000
        self.contracts = self.get_test_kontur_data(
            os.path.join(BASE_DIR, "limit/tests/test_data_kontur/test_data_contracts.json")
        )
        self.buh = self.get_test_kontur_data(os.path.join(BASE_DIR, "limit/tests/test_data_kontur/test_buh.json"))
        self.detail = self.get_test_kontur_data(os.path.join(BASE_DIR, "limit/tests/test_data_kontur/test_detail.json"))
        self.lp = LimitPrincipal(
            self.inn,
            self.start_ammount,
            data_contracts=self.contracts,
            fin_indicators=self.buh,
            info_principal=self.detail,
        )

    def get_test_kontur_data(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.loads((f.read()))

    def test_positive_get_executed_contract_last_three_year(self):
        data_last_three = self.lp.get_executed_contract_last_three_year(self.contracts)
        self.assertIsNotNone(data_last_three)
        self.assertEqual(type(data_last_three), type(list()))

    def test_negative_get_executed_contract_last_three_year(self):
        value = []
        with self.assertRaises(IndexError):
            self.lp.get_executed_contract_last_three_year(value)
        value = 5
        with self.assertRaises(TypeError):
            self.lp.get_executed_contract_last_three_year(value)

    def test_positive_get_filter_execution_completed_partially_executed(self):
        data_last_three = self.lp.get_executed_contract_last_three_year(self.contracts)
        data_filter_execute = self.lp.get_filter_execution_completed(data_last_three)
        self.assertIsNotNone(data_filter_execute)
        self.assertEqual(type(data_filter_execute), type(list()))
        data_filter_partially = self.lp.get_filter_partially_executed(data_filter_execute)
        self.assertIsNotNone(data_filter_partially)
        self.assertEqual(type(data_filter_partially), type(list()))

    def test_positive_get_sum_contract_last_three_year(self):
        result = self.lp.get_sum_contract_last_three_year(self.contracts)
        self.assertEqual(type(result), type(float()))
        result = self.lp.get_sum_contract_last_three_year([])
        self.assertEqual(type(result), type(float()))

    def test_negative_get_sum_contract_last_three_year(self):
        with self.assertRaises(AttributeError):
            self.lp.get_sum_contract_last_three_year("str")

    def test_positive_get_fin_indicator(self):
        result_1150 = self.lp.get_fin_indicator(1150, "form1")
        self.assertEqual(type(result_1150), type(int()))
        result_2120 = self.lp.get_fin_indicator(2120, "form2")
        self.assertEqual(type(result_2120), type(int()))

    # def test_negative_get_fin_indicator(self):
    #     result = self.lp.get_fin_indicator(3150, "form1")
    #     self.assertEqual(type(result), type(None))

    def test_positive_calculating_of_points(self):
        result = self.lp.calculating_of_points()
        self.assertEqual(type(result), type(dict()))
        self.assertIsNotNone(result["sos"])
        self.assertIsNotNone(result["fin_leverage"])
        self.assertIsNotNone(result["curr_liquid"])
        self.assertIsNotNone(result["ebitda"])
        self.assertIsNotNone(result["debt_load"])
        self.assertIsNotNone(result["interest_service"])
        self.assertIsNotNone(result["annual_revenue_NCC"])

    def test_negative_calculating_of_points(self):
        result = self.lp.calculating_of_points()
        with self.assertRaises(KeyError):
            result["false"]

    def test_positive_get_check_constuction(self):
        result = self.lp.get_check_constuction()
        self.assertIsNotNone(result)

    def test_positive_calculating_financial_stability(self):
        result = self.lp.calculating_financial_stability()
        self.assertEqual(type(result), type(float()))

    def test_positive_get_score_sos_constructor(self):
        self.assertEqual(self.lp.get_score_sos_constructor(0), 0.48)
        self.assertEqual(self.lp.get_score_sos_constructor(0.1), 1.6)
        self.assertEqual(self.lp.get_score_sos_constructor(-0.1), 0)

    def test_negative_get_score_sos_constructor(self):
        with self.assertRaises(TypeError):
            self.assertEqual(self.lp.get_score_sos_constructor("str"), 1)

    def test_positive_get_score_sos_not_constructor(self):
        self.assertEqual(self.lp.get_score_sos_not_constructor(0.6), 1.6)
        self.assertEqual(self.lp.get_score_sos_not_constructor(0.3), 1.12)
        self.assertEqual(self.lp.get_score_sos_not_constructor(0.15), 0.8)
        self.assertEqual(self.lp.get_score_sos_not_constructor(0.05), 0.48)
        self.assertEqual(self.lp.get_score_sos_not_constructor(0), 0.48)
        self.assertEqual(self.lp.get_score_sos_not_constructor(-0.1), 0)

    def test_positive_get_score_fin_leverage(self):
        self.assertEqual(self.lp.get_score_fin_leverage(0.5), 1.3)
        self.assertEqual(self.lp.get_score_fin_leverage(0), 1.3)
        self.assertEqual(self.lp.get_score_fin_leverage(1), 1.3)
        self.assertEqual(self.lp.get_score_fin_leverage(1.5), 0.91)
        self.assertEqual(self.lp.get_score_fin_leverage(2.5), 0.65)
        self.assertEqual(self.lp.get_score_fin_leverage(4), 0.39)
        self.assertEqual(self.lp.get_score_fin_leverage(-0.1), 0)
        self.assertEqual(self.lp.get_score_fin_leverage(6.1), 0)

    def test_positive_get_score_curr_liquid(self):
        self.assertEqual(self.lp.get_score_curr_liquid(2.1), 2)
        self.assertEqual(self.lp.get_score_curr_liquid(1.6), 1.4)
        self.assertEqual(self.lp.get_score_curr_liquid(1.3), 1)
        self.assertEqual(self.lp.get_score_curr_liquid(0.6), 0.6)
        self.assertEqual(self.lp.get_score_curr_liquid(0.4), 0)

    def test_positive_get_score_ebitda(self):
        self.assertEqual(self.lp.get_score_ebitda(21), 1.5)
        self.assertEqual(self.lp.get_score_ebitda(16), 1.05)
        self.assertEqual(self.lp.get_score_ebitda(7), 0.75)
        self.assertEqual(self.lp.get_score_ebitda(3), 0.45)
        self.assertEqual(self.lp.get_score_ebitda(-0.1), 0)

    def test_positive_get_score_debt_load(self):
        self.assertEqual(self.lp.get_score_debt_load(1), 1.7)
        self.assertEqual(self.lp.get_score_debt_load(2.5), 1.19)
        self.assertEqual(self.lp.get_score_debt_load(4), 0.85)
        self.assertEqual(self.lp.get_score_debt_load(7), 0)
        self.assertEqual(self.lp.get_score_debt_load(-0.1), 0)

    def test_positive_get_score_interest_service(self):
        self.assertEqual(self.lp.get_score_interest_service(21), 0.7)
        self.assertEqual(self.lp.get_score_interest_service(15), 0.49)
        self.assertEqual(self.lp.get_score_interest_service(3), 0.35)
        self.assertEqual(self.lp.get_score_interest_service(0), 0.35)
        self.assertEqual(self.lp.get_score_interest_service(1.8), 0.21)
        self.assertEqual(self.lp.get_score_interest_service(1), 0)
        self.assertEqual(self.lp.get_score_interest_service(-0.1), 0)

    def test_positive_get_score_annual_revenue_NCC(self):
        self.assertEqual(self.lp.get_score_annual_revenue_NCC(4), 1.2)
        self.assertEqual(self.lp.get_score_annual_revenue_NCC(3), 0.84)
        self.assertEqual(self.lp.get_score_annual_revenue_NCC(2), 0.6)
        self.assertEqual(self.lp.get_score_annual_revenue_NCC(1), 0.36)
        self.assertEqual(self.lp.get_score_annual_revenue_NCC(0.5), 0.36)
        self.assertEqual(self.lp.get_score_annual_revenue_NCC(0.4), 0)
        self.assertEqual(self.lp.get_score_annual_revenue_NCC(-0.1), 0)

    def test_positive_calculating_experience(self):
        result = self.lp.calculating_experience()
        self.assertEqual(type(result), type(float()))

    def test_positive_get_score_num_contract_big(self):
        self.assertEqual(self.lp.get_score_num_contract_big(4), 10)
        self.assertEqual(self.lp.get_score_num_contract_big(3), 10)
        self.assertEqual(self.lp.get_score_num_contract_big(2), 7)
        self.assertEqual(self.lp.get_score_num_contract_big(1), 5)
        self.assertEqual(self.lp.get_score_num_contract_big(0), 0)
        self.assertIsNone(self.lp.get_score_num_contract_big(-0.1))

    def test_positive_get_score_num_contract_all(self):
        self.assertEqual(self.lp.get_score_num_contract_all(6), 10)
        self.assertEqual(self.lp.get_score_num_contract_all(6), 10)
        self.assertEqual(self.lp.get_score_num_contract_all(3), 7)
        self.assertEqual(self.lp.get_score_num_contract_all(2), 5)
        self.assertEqual(self.lp.get_score_num_contract_all(1), 3)
        self.assertIsNone(self.lp.get_score_num_contract_all(1.5))
        self.assertIsNone(self.lp.get_score_num_contract_all(-0.1))

    def test_positive_get_score_num_of_year(self):
        self.assertEqual(self.lp.get_score_num_of_year(6), 10)
        self.assertEqual(self.lp.get_score_num_of_year(3), 5)
        self.assertEqual(self.lp.get_score_num_of_year(0), 0)
        self.assertEqual(self.lp.get_score_num_of_year(-0.1), 0)

    def test_positive_additional_factors(self):
        result = self.lp.additional_factors()
        self.assertEqual(type(result), type(dict()))

    def test_positive_get_principal_rating(self):
        rating_A = self.lp.get_principal_rating(9.1)
        self.assertEqual(rating_A["rating"], "A")
        self.assertEqual(rating_A["k"], 4.0)
        self.assertEqual(rating_A["mdo"], 50)
        rating_B = self.lp.get_principal_rating(6.6)
        self.assertEqual(rating_B["rating"], "B")
        self.assertEqual(rating_B["k"], 2.5)
        self.assertEqual(rating_B["mdo"], 35)
        rating_C = self.lp.get_principal_rating(4.5)
        self.assertEqual(rating_C["rating"], "C")
        self.assertEqual(rating_C["k"], 1.0)
        self.assertEqual(rating_C["mdo"], 20)
        rating_D = self.lp.get_principal_rating(2.5)
        self.assertEqual(rating_D["rating"], "D")
        self.assertEqual(rating_D["k"], 0)
        self.assertEqual(rating_D["mdo"], 0)

    def test_positive_limit_principal_1(self):
        result = self.lp.limit_principal_1()
        self.assertEqual(type(result), type(dict()))
        self.assertEqual(type(result["limit"]), type(float()))
        self.assertEqual(type(result["ball_rating"]), type(float()))
        self.assertEqual(type(result["letter_rating"]), type(str()))

    def test_positive_limit_principal_2(self):
        self.lp.calculating_of_points()
        self.lp.get_principal_rating(7)
        result = self.lp.limit_principal_2()
        self.assertEqual(type(result), type(float()))

    def test_positive_get_limit_principal(self):
        result = self.lp.get_limit_principal()
        self.assertEqual(type(result), type(dict()))
        self.assertEqual(type(result["limit"]), type(float()))
        self.assertEqual(type(result["ball_rating"]), type(float()))
        self.assertEqual(type(result["letter_rating"]), type(str()))
