from rest_framework.test import APITestCase

from order.tests.test_base import BaseTest


class QuoteApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_get_auction_list(self):
        url = '/api/v1/order/quote/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_auction_item(self):
        url = f'/api/v1/order/quote/{self.quote.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_positive_create_quote(self):
        url = '/api/v1/order/quote/'
        data_resp = {
            "auction": self.auction.id,
            "bank": self.bank.id,
            "guarantee_rate": 1.2,
            "guarantee_sum": 82237313,
            "bank_rate": 1.2,
            "bank_sum": 989551.45,
            "insurance_premium_rate": 0.8,
            "insurance_premium_sum": 659700.97,
            "master_agent_rate": 0.08,
            "master_agent_sum": 65970.10,
            "agent_rate": 1.12,
            "agent_sum": 923581.35,
            "type": "Авто",
            "status": "Первичная",
            "expiry_date": '2021-08-17'
        }
        response = self.client.post(url, data=data_resp)
        self.assertEqual(response.status_code, 201, )

    def test_positive_update_quote(self):
        quote_id = self.quote.id
        url = f'/api/v1/order/quote/{quote_id}/'
        partial_data = {
            'bank_rate': 10,
            "expiry_date": '2021-08-20'
        }
        response = self.client.put(url, data=partial_data)
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_sum_quote(self):
        url = '/api/v1/order/quote/get_sum/'
        data_resp = {
            "sum": 1000,
            "rate": 2
        }
        response = self.client.post(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )
