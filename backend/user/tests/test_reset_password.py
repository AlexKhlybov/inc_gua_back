from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from rest_framework.test import APIClient, APITestCase
from ..models.pages import ChangePassword


class ResetPasswordTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='butcher228@322berezin.com',
            password='EtotTestRabotaetVopros',
            phone='88005553535',
            is_staff=True,
            is_superuser=True,
            first_name='Семен',
            last_name='Свалов',
        )
        self.page = ChangePassword.objects.get_or_create(
            title='qweqwe',
            slug='qweqwe',
        )[0]
        self.page.sites.add(Site.objects.first())
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_positive_reset_password_link(self):
        response = self.client.post('/api/v1/user/user/get_reset_password_link/', data={'email': self.user.email})
        self.assertEqual(response.status_code, 200, )
        response = self.client.post(
            '/api/v1/user/user/reset_password/',
            data={
                'reset_link': self.user.generate_link(),
                'password': self.user.password,
            }
        )
        self.assertEqual(response.status_code, 200, )

    def test_negative_reset_password_link(self):
        response = self.client.post('/api/v1/user/user/get_reset_password_link/', data={'email': 'test'})
        self.assertEqual(response.status_code, 400, )
        response = self.client.post('/api/v1/user/user/get_reset_password_link/', data={'email': self.user.email})
        self.assertEqual(response.status_code, 200, )
        response = self.client.post(
            '/api/v1/user/user/reset_password/',
            data={
                'reset_link': '',
                'password': '',
            }
        )
        self.assertEqual(response.status_code, 400, )
