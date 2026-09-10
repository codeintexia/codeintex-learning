import json

from django.contrib.auth import get_user_model
from django.test import Client, TestCase


class AuthApiTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="auth-learner",
            password="test-only-password",
        )

    def test_session_reports_anonymous_user(self):
        response = self.client.get(
            "/api/v1/auth/session/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["authenticated"])
        self.assertIsNone(response.json()["user"])

    def test_login_rejects_invalid_credentials(self):
        response = self.client.post(
            "/api/v1/auth/login/",
            data=json.dumps(
                {
                    "username": "auth-learner",
                    "password": "wrong-password",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 401)

    def test_login_establishes_session(self):
        login_response = self.client.post(
            "/api/v1/auth/login/",
            data=json.dumps(
                {
                    "username": "auth-learner",
                    "password": "test-only-password",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(login_response.status_code, 200)
        self.assertTrue(login_response.json()["authenticated"])

        session_response = self.client.get(
            "/api/v1/auth/session/"
        )

        self.assertTrue(
            session_response.json()["authenticated"]
        )
        self.assertEqual(
            session_response.json()["user"]["username"],
            "auth-learner",
        )

    def test_logout_clears_session(self):
        self.client.force_login(self.user)

        response = self.client.post(
            "/api/v1/auth/logout/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["authenticated"])

        session_response = self.client.get(
            "/api/v1/auth/session/"
        )

        self.assertFalse(
            session_response.json()["authenticated"]
        )

    def test_login_is_csrf_protected(self):
        client = Client(enforce_csrf_checks=True)

        rejected = client.post(
            "/api/v1/auth/login/",
            data=json.dumps(
                {
                    "username": "auth-learner",
                    "password": "test-only-password",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(rejected.status_code, 403)

        csrf_response = client.get(
            "/api/v1/auth/csrf/"
        )
        csrf_token = csrf_response.json()["csrfToken"]

        accepted = client.post(
            "/api/v1/auth/login/",
            data=json.dumps(
                {
                    "username": "auth-learner",
                    "password": "test-only-password",
                }
            ),
            content_type="application/json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(accepted.status_code, 200)
