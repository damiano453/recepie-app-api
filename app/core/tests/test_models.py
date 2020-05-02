from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = "test@damiano453.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    ''' recommended (domain is case insensitive) '''
    def test_new_user_email_normalize(self):
        """ Test the email for a new user us normalized """
        email = "test@DAMIANO453.COM"
        user = get_user_model().objects.create_user(
            email,
            'test123'          # just to be, cheking email field
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                'test123'      # just to be, cheking email field
            )

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        superuser = "super@damiano453.com"
        password = "password1234"
        user = get_user_model().objects.create_superuser(
            email=superuser,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
