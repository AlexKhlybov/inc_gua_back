from rest_framework.test import APITestCase

from .test_base import BaseTest


class OliverWymanReportApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)
        self.supplier = self.principal
        self.customer = self.beneficiary

    def test_positive_olyver_wyman(self):
        url = '/api/v1/order/oliver_wyman/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )
