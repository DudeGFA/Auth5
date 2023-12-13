# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     BaseUserManager,
#     PermissionsMixin,
# )
from django.utils.translation import gettext_lazy as _
from helpers.models import TimestampsModel
from django.db import models
import uuid
from django.contrib.auth.models import User

class Website(models.Model):
    link = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='website')
    callback_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    websites = models.ManyToManyField(Website, through='WebsiteAccount', related_name='website_user_profiles')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class FieldGroup(models.Model):
    name = models.CharField(max_length=25)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'name']

    def __str__(self):
        return f"{self.name} (Owner: {self.owner})"

class Field(models.Model):
    did = models.CharField(max_length=2000, null=True, blank=True)
    recordid = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=25)
    group = models.ForeignKey(FieldGroup, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['group', 'name']

    def __str__(self):
        return f"{self.group}-{self.name} (Owner: {self.group.owner})"

class WebsiteAccount(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    user_id_on_website = models.CharField(max_length=255)
    field_group = models.ForeignKey(FieldGroup, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return f"{self.user_profile.user.username}'s Account on {self.website.name}"



# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         return self.create_user(email, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin, TimestampsModel):
#     # email = models.EmailField(_("email address"), unique=True)
#     is_active = models.BooleanField(_("active"), default=True)
#     is_staff = models.BooleanField(_("staff status"), default=False)
#     is_owner = models.BooleanField(_("owner status"), default=False)
#     user_id = models.UUIDField(default=uuid.uuid4, editable=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = "user_id"