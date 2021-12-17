from rest_framework.test import APITestCase

from order.tests.test_base import BaseTest


class OrderQuoteApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_state_log(self):
        url = '/api/v1/order/order_quote/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )
