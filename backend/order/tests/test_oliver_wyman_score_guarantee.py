import os

from rest_framework.test import APITestCase

from order.tests.test_base import BaseTest


class OliverWymanApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)
        self.supplier = self.principal
        self.customer = self.beneficiary

    def test_positive_olyver_wyman_score_guarantee(self):
        if not os.getenv('OW_URL') or not os.getenv('OW_LOGIN') or not os.getenv('OW_PASSWORD'):
            response = self.client.post('/api/v1/order/order/olyver_wyman_score_guarantee/',
                                        data={
                                            "supplierInn": self.legal_entity_principal.inn,
                                            "customerInn": self.legal_entity_beneficiary.inn,
                                            "reportType": "Y"
                                        })
            self.assertEqual(response.status_code, 400, )
        else:
            response = self.client.post('/api/v1/order/order/olyver_wyman_score_guarantee/',
                                        data={
                                            "supplierInn": self.legal_entity_principal.inn,
                                            "customerInn": self.legal_entity_beneficiary.inn,
                                            "reportType": "Y"
                                        })
            self.assertEqual(response.status_code, 200, )
    #
    # def test_negative_client_olyver_wyman_score_guarantee(self):
    #     if os.getenv('OW_URL') or not os.getenv('OW_LOGIN') or not os.getenv('OW_PASSWORD'):
    #         response = self.client_principal.post('/api/v1/order/order/olyver_wyman_score_guarantee/',
    #                                               data={
    #                                                   "supplierInn": self.legal_entity_principal.inn,
    #                                                   "customerInn": self.legal_entity_beneficiary.inn,
    #                                                   "reportType": "Y"
    #                                               })
    #         self.assertEqual(response.status_code, 403, )

    def test_negative_olyver_wyman_score_guarantee(self):
        response = self.client.post('/api/v1/order/order/olyver_wyman_score_guarantee/',
                                    data={'supplierInn': 3222281337,
                                          })
        self.assertEqual(response.status_code, 400, )
