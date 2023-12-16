from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("Account.urls")),
    path("authentication/", include("authentication.urls", namespace="authentication")),
    path("", include("dashboard.urls", namespace="dashboard")),
]