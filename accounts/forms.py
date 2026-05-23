from django.contrib.auth import get_user_model
from django.contrib.auth import forms as forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms as django_forms

from accounts.models import Profile

UserModel = get_user_model()

class AppUserCreationForm(forms.UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class AppUserChangeForm(forms.UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileForm(django_forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
