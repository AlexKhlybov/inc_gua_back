from rest_framework.test import APITestCase
from order.tests.test_base import BaseTest


class LotApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_get_lot_list(self):
        url = '/api/v1/order/lot/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_lot_item(self):
        url = f'/api/v1/order/lot/{self.lot.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_notexist_get_lot_item(self):
        url = f'/api/v1/order/lot/{self.bad_id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, )
