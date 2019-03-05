from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""
        email = 'test@test.com'
        password = '123testing'
        user = get_user_model().objects.create_user(
            email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ TEST the email for the new user is normalized """
        email = 'test@LONDONAPP.COM'
        user = get_user_model().objects.create_user(email, '123testing')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_user_is_superuser(self):
        user = get_user_model().objects.create_superuser('zoki@zoki.com', '123testing')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
