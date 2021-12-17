from rest_framework.test import APITestCase

from .test_base import BaseTest


class FactorsApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_factors(self):
        url = '/api/v1/order/factors/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_positive_update_factors(self):
        factor_id = self.factors.id
        url = f'/api/v1/order/factors/{factor_id}/'
        data_resp = {
            'value': True
        }
        response = self.client.patch(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )
