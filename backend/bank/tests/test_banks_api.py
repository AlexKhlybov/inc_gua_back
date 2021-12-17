from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from ..models.bank import Bank


class BankApiTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@gg.com',
            password='SuPerPasSwOrd12345',
            phone='89969185053',
            is_staff=True,
            is_superuser=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_positive_get_banks(self):
        url = '/api/v1/bank/bank/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_bank_documents(self):
        url = '/api/v1/bank/bank_document/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_bank_limits(self):
        url = '/api/v1/bank/bank_limits/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_bank_contract(self):
        url = '/api/v1/bank/bank_contract/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )


class BankLimitsApiTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@gg.com',
            password='SuPerPasSwOrd12345',
            phone='89969185053',
            is_staff=True,
            is_superuser=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.bank = Bank.objects.get_or_create(id=1)[0]

    def test_positive_update_bank_limits(self):
        url = '/api/v1/bank/bank_limits/update_bank_limits/'
        response = self.client.post(f'{url}',
                                    data={
                                        "bank": 1
                                    })
        self.assertEqual(response.status_code, 200, )
