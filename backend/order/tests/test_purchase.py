from rest_framework.test import APITestCase
from order.tests.test_base import BaseTest


class PurchaseApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_get_purchase_list(self):
        url = '/api/v1/order/purchase/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_purchase_item(self):
        url = f'/api/v1/order/purchase/{self.purchase.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_notexist_get_purchase_item(self):
        url = f'/api/v1/order/purchase/{self.bad_id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, )
