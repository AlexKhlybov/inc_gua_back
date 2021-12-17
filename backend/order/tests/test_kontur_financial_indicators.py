import os

from rest_framework.test import APITestCase

from entity.models import Principal, LegalEntity
from order.tests.test_base import BaseTest


class KonturApiTest(APITestCase, BaseTest):
    def setUp(self):
        BaseTest.__init__(self)
        legal_entity = LegalEntity.objects.get_or_create(inn='123456789014')[0]
        self.principal = Principal.objects.get_or_create(legal_entity=legal_entity)[0]

    def test_positive_kontur_financial_indicators(self):
        if not os.getenv('KONTUR_KEY') or not os.getenv('KONTUR_URL'):
            response = self.client.post('/api/v1/order/order/kontur_financial_indicators/',
                                        data={'inn': self.principal.legal_entity.inn})
            self.assertEqual(response.status_code, 400, )
        else:

            response = self.client.post('/api/v1/order/order/kontur_financial_indicators/',
                                        data={'inn': self.principal.legal_entity.inn})
            self.assertEqual(response.status_code, 200, )

    def test_negative_client_kontur_financial_indicators(self):
        if os.getenv('KONTUR_KEY') or not os.getenv('KONTUR_URL'):
            response = self.client_principal.post('/api/v1/order/order/kontur_financial_indicators/',
                                                  data={'inn': self.principal.legal_entity.inn})
            self.assertEqual(response.status_code, 403, )

    def test_negative_kontur_financial_indicators(self):
        response = self.client.post('/api/v1/order/order/kontur_financial_indicators/',
                                    data={'inn': 3222281337,
                                          })
        self.assertEqual(response.status_code, 400, )
