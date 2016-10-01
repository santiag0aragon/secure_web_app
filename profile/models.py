# # -*- coding: utf-8 -*-

# from django.db import models
# from django.contrib.auth.models import User


# # class Client(models.Model):
# #     company = models.CharField(
# #         max_length=50,
# #         verbose_name='Compañía',
# #         blank=False
# #     )
# #     logo = models.ImageField(
# #         null=True,
# #         default=None,
# #         blank=True
# #     )
# #     web_site = models.CharField(
# #         max_length=50,
# #         verbose_name='Sitio web',
# #         blank=True
# #     )
# #     client_since = models.DateField(
# #         verbose_name='Cliente desde',
# #         blank=True,
# #         null=True
# #     )
# #     description = models.TextField(
# #         verbose_name='Descripción',
# #         blank=True,
# #         null=True
# #     )

# #     def __unicode__(self):
# #         return self.company

# #     class Meta:
# #         verbose_name = 'Cliente'
# #         verbose_name_plural = 'Clientes'
# #         ordering = ['client_since']


# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         User,
#         verbose_name='usuario',
#         blank=False
#     )

#     def __unicode__(self):
#         return str(self.user)

#     class Meta:
#         verbose_name = 'User profile'
#         verbose_name_plural = 'User Profiles'


# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
