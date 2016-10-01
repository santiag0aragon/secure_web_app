# import factory
# from django.test import TestCase, RequestFactory, Client
# from django.contrib.auth.models import User, Group
# from datata_profile.models import UserProfile
# from django.contrib.auth.models import AnonymousUser
# from django.core.urlresolvers import reverse
# from datata_notification.views import *


# class UserProfileTestViews(TestCase):

#     def setUp(self):
#         self.factory = RequestFactory()
#         self.password = 'top_secret'
#         self.user = User.objects.create_user(
#             username='test_user',
#             first_name='test_name',
#             email='test@a.com',
#             password=self.password)
#         self.group = Group.objects.create(
#             name='test_group')
#         self.user_notification = NotificationUser.objects.create(
#             title='test_title',
#             message='test_message_user',
#             user=self.user)
#         self.group_notification = NotificationGroup.objects.create(
#             title='test_title',
#             message='test_message_group',
#             group=self.group)
#         self.profile = UserProfile.objects.get_or_create(
#             user=self.user,
#             color_background='EEEEEE')
#         self.client = Client()

#     def show_notification_user_nologin_test(self):
#         response = self.client.post(
#                                 reverse(show_notification,
#                                         kwargs={'notification_id':
#                                                 self.user_notification.id,
#                                                 'type': '1'}))
#         self.assertEqual(response.status_code, 302)

#     def show_notification_group_nologin_test(self):
#         response = self.client.post(
#                                 reverse(show_notification,
#                                         kwargs={'notification_id':
#                                                 self.group_notification.id,
#                                                 'type': '1'}))
#         self.assertEqual(response.status_code, 302)

#     def show_notification_user_test(self):
#         self.client.login(username=self.user.username, password=self.password)
#         response = self.client.post(
#                                 reverse(show_notification,
#                                         kwargs={'notification_id':
#                                                 self.user_notification.id,
#                                                 'type': '0'}))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.user_notification.message)

#     def show_notification_group_test(self):
#         self.client.login(username=self.user.username, password=self.password)
#         response = self.client.post(
#                                 reverse(show_notification,
#                                         kwargs={'notification_id':
#                                                 self.group_notification.id,
#                                                 'type': '1'}))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.group_notification.message)

#     def del_notification_user_test(self):
#         self.client.login(username=self.user.username, password=self.password)
#         self.assertFalse(self.user_notification.viewed)
#         response = self.client.post(
#                                 reverse(delete_notification,
#                                         kwargs={'notification_id':
#                                                 self.user_notification.id,
#                                                 'type': '0'}))
#         self.assertEqual(response.status_code, 302)
#         new_not = NotificationUser.objects.get(
#                                         id=self.user_notification.id).viewed
#         self.assertTrue(new_not)

#     def del_notification_group_test(self):
#         self.client.login(username=self.user.username, password=self.password)
#         self.assertFalse(self.group_notification.viewed)
#         response = self.client.post(
#                                 reverse(delete_notification,
#                                         kwargs={'notification_id':
#                                                 self.group_notification.id,
#                                                 'type': '1'}))
#         self.assertEqual(response.status_code, 302)
#         new_not = NotificationGroup.objects.get(
#                                         id=self.group_notification.id).viewed
#         self.assertTrue(new_not)

#     def del_notification_group_nologin_test(self):
#         self.assertFalse(self.group_notification.viewed)
#         response = self.client.post(
#                                 reverse(delete_notification,
#                                         kwargs={'notification_id':
#                                                 self.group_notification.id,
#                                                 'type': '1'}))
#         new_not = NotificationGroup.objects.get(
#                                         id=self.group_notification.id).viewed
#         self.assertFalse(new_not)

#     def del_notification_user_nologin_test(self):
#         self.assertFalse(self.user_notification.viewed)
#         response = self.client.post(
#                                 reverse(delete_notification,
#                                         kwargs={'notification_id':
#                                                 self.user_notification.id,
#                                                 'type': '0'}))
#         new_not = NotificationUser.objects.get(
#                                         id=self.user_notification.id).viewed
#         self.assertFalse(new_not)
