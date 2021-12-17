from rest_framework.test import APITestCase
from order.tests.test_base import BaseTest


class ContestTypeApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_get_contest_type_list(self):
        url = '/api/v1/order/contest_type/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_contest_type_item(self):
        url = f'/api/v1/order/contest_type/{self.type.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_notexist_get_contest_type_item(self):
        url = f'/api/v1/order/contest_type/{self.bad_id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, )
