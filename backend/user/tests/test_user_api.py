from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase


class UserApiTest(APITestCase):
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

    def test_positive_get_user_users(self):
        url = '/api/v1/user/user/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_user_get_underwriter_list(self):
        url = '/api/v1/user/user/get_underwriter_list/'
        response = self.client.get(f'{url}')
        self.assertEqual(response.status_code, 200, )

    def test_positive_update_user_users(self):
        user_id = self.user.id
        url = f'/api/v1/user/user/{user_id}/'
        data_resp = {
            'authority': 5000
        }
        response = self.client.patch(url, data=data_resp)
        self.assertEqual(response.status_code, 200, )
