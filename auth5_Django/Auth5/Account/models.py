from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from helpers.models import TimestampsModel
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin, TimestampsModel):
    email = models.EmailField(_("email address"), unique=True)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_owner = models.BooleanField(_("owner status"), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

class WebSite(TimestampsModel):
    name = models.CharField(max_length=255)
    link = models.URLField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='websites')

    def __str__(self):
        return self.name
    
class UserProfile(TimestampsModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    websites = models.ManyToManyField('Website', through='WebsiteAccount', related_name='user_profiles')

    def __str__(self):
        return f"{self.user.email}'s Profile"
    

class WebsiteAccount(TimestampsModel):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    website = models.ForeignKey(WebSite, on_delete=models.CASCADE)
    user_id_on_website = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.email}'s Account on {self.website.name}"