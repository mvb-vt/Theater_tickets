from django.db import models
from django.contrib.auth import models as auth_models, get_user_model
from accounts.manager import AppUserManager
from phonenumber_field.modelfields import PhoneNumberField

class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(unique=True, blank=False, null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(
        max_length=30,
        blank=True, null=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True, null=True,
    )
    phone_number = PhoneNumberField(
        unique=True, region="BG"
    )