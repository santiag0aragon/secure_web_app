# from django import forms
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Field, Layout
# from crispy_forms.bootstrap import FormActions

# # from models import UserProfile


# # class UserProfileForm(forms.ModelForm):
# #     helper = FormHelper()
# #     helper.form_method = 'POST'
# #     helper.form_class = 'form-horizontal'
# #     helper.layout = Layout(
# #         Field('color_background', css_class='color'),
# #         Field('color_link', css_class='color'),
# #         Field('color_active_tab', css_class='color'),
# #         FormActions(Submit('save', 'Guardar', css_class='btn-primary'))
# #     )

# #     class Meta:
# #         model = UserProfile
# #         fields = (
# #             "color_background",
# #             "color_link",
# #             "color_active_tab",
# #         )
# #         labels = {
# #             'color_background': _('Color de fondo'),
# #             'color_link': _('Color de ligas'),
# #             'color_active_tab': _('Color de elemento activo'),
# #         }


# # class RegistrationForm(UserCreationForm):
# #     email = forms.EmailField(required=True)

# #     class Meta:
# #         model = User
# #         fields = ("username", "email","password1", "password2")

# #     def save(self, commit=True):
# #         user = super(RegistrationForm, self).save(commit=False)
# #         user.email = self.cleaned_data["email"]
# #         if commit:
# #             # puede ser que sea necesario un wrapper para los permisos, la logica iria aqui
# #             #
# #             # from django.contrib.auth.models import User, Group, Permission
# #             # from django.contrib.contenttypes.models import ContentType
# #             # content_type = ContentType.objects.get(app_label='myapp', model='BlogPost')
# #             # permission = Permission.objects.create(codename='can_publish',
# #             #                           name='Can Publish Posts',
# #             #                           content_type=content_type)
# #             #
# #             # user = User.objects.get(username='duke_nukem')
# #             # group = Group.objects.get(name='wizard')
# #             # group.permissions.add(permission)
# #             # user.groups.add(group)

# #             user.save()
# #         return user
