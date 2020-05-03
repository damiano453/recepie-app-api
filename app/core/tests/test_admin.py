from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """ setup running before any test in this class start """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@damiano453.com',
            password='pass12345'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@damiano453.com',
            password='password111',
            name='Test user full name'
        )

    def test_users_listed(self):
        """ Test that users are listed on user page """
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """ Test that user edit page works """
        url = reverse('admin:core_user_change', args=[self.user.id])
        # f.e. url = /admin/core/userid/
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """ Test creation of user page """
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
