import factory
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from datata_profile.models import UserProfile
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from datata_profile.views import *


class UserProfileTestViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.password = 'top_secret'
        self.user = User.objects.create_user(
            username='test_user',
            first_name='test_name',
            email='test@a.com',
            password=self.password)
        self.profile = UserProfile.objects.get_or_create(
            user=self.user,
            color_background='EEEEEE')
        self.client = Client()

    def test_login(self):
        response = self.client.get(reverse(invalid_login))
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.get(reverse(login))
        self.assertEqual(response.status_code, 200)

    def test_login_false(self):
        response = self.client.post(
                                reverse(auth_view),
                                {'username': self.user.username,
                                 'password': 'fake_pass'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('LOCATION', ''),
                         'http://testserver/accounts/invalid/')

    def test_login_true(self):
        response = self.client.post(
                                reverse(auth_view),
                                {'username': self.user.username,
                                 'password': self.password})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('LOCATION', ''),
                         'http://testserver/demo/')

    def test_user_profile_get(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse(user_profile))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['first_name'],
                         'test_name')

    def test_user_profile_post(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(reverse(user_profile),
                                    {'color_background': 'FFFFFF',
                                     'color_link': 'FFFFFF',
                                     'color_active_tab': 'FFFFFF'})
        new_color = UserProfile.objects.get(user=self.user).color_background

        self.assertEqual(new_color, 'FFFFFF')

    def test_logout(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse(logout))
        is_auth = response.context['user'].is_authenticated()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(is_auth)

    def test_profile(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse(profile))
        self.assertEqual(response.context['first_name'],
                         'test_name')
        self.assertEqual(self.profile[0].color_background, 'EEEEEE')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.user.delete()
        self.profile[0].delete()
