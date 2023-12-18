from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("userprofile/<str:id>/", views.UserProfileView.as_view(), name="userprofile"),
    path("login/", views.LoginView.as_view()),
    path("callback/", views.CallbackView.as_view()),
]
