from rest_framework.test import APITestCase
from order.tests.test_base import BaseTest


class AuctionApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)

    def test_positive_get_auction_list(self):
        url = '/api/v1/order/auction/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_auction_item(self):
        url = f'/api/v1/order/auction/{self.auction.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )

    def test_notexist_get_auction_item(self):
        item_id = 10
        url = f'/api/v1/order/auction/{item_id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, )
