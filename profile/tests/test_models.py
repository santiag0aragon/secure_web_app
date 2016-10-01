import factory
from django.test import TestCase
from django.contrib.auth.models import User

from datata_profile.models import UserProfile
from datata_profile.models import Client as clt


class UserProfileTestsModels(TestCase):
    def setUp(self):
        self.clt = clt.objects.create(
            company='test_company')
        self.user = User.objects.create_user(
            username='test_user',
            first_name='test_name',
            email='test@a.com',
            password='top_secret')
        self.profile = UserProfile.objects.get_or_create(
            user=self.user,
            color_background='EEEEEE')

    def tearDown(self):
        self.clt.delete()

    def test_client_print(self):
        self.assertEqual(str(self.clt), 'test_company')

    def test_user_profile_print(self):
        self.assertEqual(str(self.profile[0]), 'test_user')
