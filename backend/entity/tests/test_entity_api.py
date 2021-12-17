from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase


class EntityApiTest(APITestCase):
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

    def test_positive_get_entity_beneficiary(self):
        url = '/api/v1/entity/beneficiary/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_entity_principal(self):
        url = '/api/v1/entity/principal/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_legal_entity(self):
        url = '/api/v1/entity/legal_entity/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_person(self):
        url = '/api/v1/entity/person/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_co_owner(self):
        url = '/api/v1/entity/co_owner/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_ownership(self):
        url = '/api/v1/entity/ownership/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )
