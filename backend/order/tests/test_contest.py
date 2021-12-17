from rest_framework.test import APITestCase
from order.tests.test_base import BaseTest


class ContestApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_get_contest_list(self):
        url = '/api/v1/order/contest/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_contest_item(self):
        url = f'/api/v1/order/contest/{self.contest.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_notexist_get_contest_item(self):
        url = f'/api/v1/order/contest/{self.bad_id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, )
