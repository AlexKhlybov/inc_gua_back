from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase

from ..models import LimitFZ, FZLimits, LimitPrincipalModel
from entity.models import Principal, LegalEntity


class LimitApiTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gg.com", password="SuPerPasSwOrd12345", phone="89969185053", is_staff=True, is_superuser=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_positive_get_limit_limit_bank(self):
        url = "/api/v1/limit/limit_bank/"
        response = self.client.get(f"{url}")
        self.assertEqual(
            response.status_code,
            200,
        )

    def test_positive_get_limit_limit_fz(self):
        url = "/api/v1/limit/limit_fz/"
        response = self.client.get(f"{url}")
        self.assertEqual(
            response.status_code,
            200,
        )

    def test_positive_get_limit_limit(self):
        url = "/api/v1/limit/limit/"
        response = self.client.get(f"{url}")
        self.assertEqual(
            response.status_code,
            200,
        )

    def test_positive_get_limit_limit_principal(self):
        url = "/api/v1/limit/limit_principal/"
        response = self.client.get(f"{url}")
        self.assertEqual(
            response.status_code,
            200,
        )


class FZLimitsApiTest(APITestCase):
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
        self.fz = LimitFZ.objects.create(fz='ФЗ-тест')
        fz_limits = FZLimits.objects.filter(fz=self.fz)
        if not fz_limits:
            fz_limits = FZLimits(fz=self.fz)
            fz_limits.save()
        self.fz_limits = fz_limits

    def test_positive_update_fz_limits(self):
        url = '/api/v1/limit/fz_limits/update_fz_limits/'
        response = self.client.post(f'{url}',
                                    data={
                                        "fz": self.fz.id
                                    })
        self.assertEqual(response.status_code, 200, )

    def test_positive_get_fz_limits(self):
        url = "/api/v1/limit/fz_limits/"
        response = self.client.get(f"{url}")
        self.assertEqual(
            response.status_code,
            200,
        )

    def test_positive_get_fz_limits_instance(self):
        url = f'/api/v1/limit/fz_limits/{self.fz_limits.id}/'
        response = self.client.get(f"{url}")
        self.assertEqual(
            response.status_code,
            200,
        )


class PrincipalLimitsApiTest(APITestCase):
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
        self.legal_entity_principal = LegalEntity.objects.create(
            inn='123456789013',
            region='Иваново',
            okved='15.55.67',
        )
        self.principal = Principal.objects.create(
            title='Петя',
            legal_entity=self.legal_entity_principal,
        )
        principal_limits = LimitPrincipalModel.objects.filter(principal=self.principal)
        if not principal_limits:
            principal_limits = LimitPrincipalModel(principal=self.principal)
            principal_limits.save()
        self.principal_limits = principal_limits

    def test_positive_update_principal_limits(self):
        url = '/api/v1/limit/limit_principal/update_principal_limits/'
        response = self.client.post(f'{url}',
                                    data={
                                        "principal": self.principal.id
                                    })
        self.assertEqual(response.status_code, 200, )
