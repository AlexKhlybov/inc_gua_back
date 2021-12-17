from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase


class AuthTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@gg.com',
            password='SuPerPasSwOrd12345',
            phone='89969185053',
            is_staff=True,
            is_superuser=True,
            first_name='Семен',
            last_name='Свалов',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_positive_crate_token_login_email(self):
        url = '/api/v1/login/'
        response = self.client.post(f'{url}', data={"email": "test@gg.com", "password": "SuPerPasSwOrd12345"})
        self.assertEqual(response.status_code, 200, )

    def test_negative_crate_token_login_email(self):
        url = '/api/v1/login/'
        response = self.client.post(f'{url}', data={"email": "test@gg.com", "password": "wrong_password"})
        self.assertEqual(response.status_code, 400, )
