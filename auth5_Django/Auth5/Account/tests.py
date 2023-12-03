from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser


class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.refresh_url = reverse("login_refresh")

        self.user_data = {
            "email": "testuser@example.com",
            "password": "testpassword",
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, "testuser@example.com")

    def test_user_registration_invalid_data(self):
        invalid_data = {
            "email": "invalidemail",
            "password": "testpassword",
        }

        response = self.client.post(self.register_url, invalid_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_user_registration_missing_required_field(self):
        url = reverse("register")
        data_missing_required_field = {
            # 'email': 'testuser@example.com', # Missing required field
            "password": "testpassword",
        }

        response = self.client.post(url, data_missing_required_field, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_user_login(self):
        self.client.post(self.register_url, self.user_data, format="json")

        login_data = {
            "email": "testuser@example.com",
            "password": "testpassword",
        }

        login_response = self.client.post(self.login_url, login_data, format="json")

        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.assertIn("access", login_response.data)
        self.assertIn("refresh", login_response.data)

    def test_user_login_invalid_credentials(self):
        self.client.post(self.register_url, self.user_data, format="json")

        invalid_login_data = {
            "email": "testuser@example.com",
            "password": "wrongpassword",
        }

        invalid_login_response = self.client.post(
            self.login_url, invalid_login_data, format="json"
        )

        self.assertEqual(
            invalid_login_response.status_code, status.HTTP_401_UNAUTHORIZED
        )
        self.assertNotIn("access", invalid_login_response.data)
        self.assertNotIn("refresh", invalid_login_response.data)

    def test_user_token_refresh(self):
        self.client.post(self.register_url, self.user_data, format="json")

        login_data = {
            "email": "testuser@example.com",
            "password": "testpassword",
        }
        login_response = self.client.post(self.login_url, login_data, format="json")
        refresh_token = login_response.data["refresh"]

        refresh_data = {"refresh": refresh_token}
        refresh_response = self.client.post(
            self.refresh_url, refresh_data, format="json"
        )

        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn("access", refresh_response.data)

    def test_user_token_refresh_invalid_token(self):
        invalid_refresh_data = {"refresh": "invalid_refresh_token"}
        invalid_refresh_response = self.client.post(
            self.refresh_url, invalid_refresh_data, format="json"
        )

        self.assertEqual(
            invalid_refresh_response.status_code, status.HTTP_401_UNAUTHORIZED
        )
        self.assertNotIn("access", invalid_refresh_response.data)
