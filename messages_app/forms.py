from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from models import NotificationUser


class NotificationForm(forms.ModelForm):

    class Meta:
        model = NotificationUser
        fields = ('title', 'message', 'user')
