from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path("dashboard/website/", views.WebsiteDashboardView.as_view(), name="website-dashboard"),
    path("dashboard/<str:group>/", views.HomeView.as_view()),
    path("dashboard/", views.HomeView.as_view()),
    path("fetch/<str:website_name>/<int:data_owner_id>", views.FetchDataView.as_view()),
    path("", views.LandingView.as_view()),
]