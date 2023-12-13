from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path("website/", views.WebsiteDashboardView.as_view(), name="website-dashboard"),
    path("<str:group>", views.HomeView.as_view()),
    path("", views.HomeView.as_view()),
]