from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.RegistrationAPIView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/refresh/", views.LoginRefreshView.as_view(), name="login_refresh"),
    path("logout/", views.LogoutAPIView.as_view(), name="logout"),
]
