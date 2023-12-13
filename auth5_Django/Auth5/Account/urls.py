from django.urls import path
from . import views

urlpatterns = [
    path("api-register/", views.RegistrationAPIView.as_view(), name="api-register"),
    path("register/", views.RegistrationFormView.as_view(), name="register"),
    path("website/register/", views.WebsiteRegistrationFormView.as_view(), name="website-register"),
    path("website/login/", views.WebsiteLoginFormView.as_view(), name="website-login"),
    path("api-login/", views.LoginView.as_view(), name="api-login"),
    path("api-login/refresh/", views.LoginRefreshView.as_view(), name="api-login_refresh"),
    path("api-logout/", views.LogoutAPIView.as_view(), name="api-logout"),
    path("login/", views.LoginFormView.as_view(), name="login"),
]
