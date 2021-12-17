from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase

from ..models.changelog import ChangeLog


class ChangeLogApiTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gg.com", password="SuPerPasSwOrd12345", phone="89969185053", is_staff=True, is_superuser=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.changelog = ChangeLog.objects.create(
            user=self.user, role="underwriter", action_on_model=ChangeLog.ACTIONS.ACTION_CREATE, name="Заявка №7"
        )
        self.bad_id = 10

    def test_positive_get_changelog_list(self):
        url = "/api/v1/changelog/changelog/"
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            200,
        )

    def test_positive_get_changelog_item(self):
        url = f"/api/v1/changelog/changelog/{self.changelog.id}/"
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            200,
        )

    def test_notexist_get_changelog_item(self):
        url = f"/api/v1/changelog/changelog/{self.bad_id}/"
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            404,
        )
