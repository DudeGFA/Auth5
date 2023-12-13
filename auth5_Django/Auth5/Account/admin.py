from django.contrib import admin
from Account.models import Website, WebsiteAccount, UserProfile, Field, FieldGroup
# from django.contrib.auth import get_user_model

# UserModel = get_user_model()


# @admin.register(UserModel)
# class UserModelAdmin(admin.ModelAdmin):
#     model = UserModel
#     list_display = ("email",)
admin.site.register(Website)
admin.site.register(WebsiteAccount)
admin.site.register(UserProfile)
admin.site.register(Field)
admin.site.register(FieldGroup)