from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("Account.urls")),
    path("authentication/", include("authentication.urls", namespace="authentication")),
    path("", include("dashboard.urls", namespace="dashboard")),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)