from django.urls import path
from . import views

app_name="authentication"
urlpatterns = [
    path("<str:website_name>/", views.AuthenticateView.as_view()),
    path("<str:website_name>/validate_token/", views.ValidateTokenView.as_view()),
]
