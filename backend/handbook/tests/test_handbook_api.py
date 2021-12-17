from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase


class HandbookApiTest(APITestCase):
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

    def test_positive_get_handbook_black_list_item(self):
        url = '/api/v1/handbook/black_list_item/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )
