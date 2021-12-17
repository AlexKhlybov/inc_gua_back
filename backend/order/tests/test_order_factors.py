from rest_framework.test import APITestCase

from .test_base import BaseTest


class OrderFactorsApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_factors(self):
        url = '/api/v1/order/order_factors/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )
