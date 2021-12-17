from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase


class StateLogApiTest(APITestCase):
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

    def test_positive_state_log(self):
        url = '/api/v1/order/state_log/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, )
