from django.urls import path
from . import views

urlpatterns = [
    path("userprofile/<int:id>/", views.UserProfileView.as_view(), name="userprofile"),
    path("login/", views.LoginView.as_view())
]
