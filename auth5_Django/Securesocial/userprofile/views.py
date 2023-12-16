from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
import requests
from django.contrib.auth import authenticate, login

# Create your views here.
class UserProfileView(View):
    def get(self, request, id):
        return render(request, "profile_page.html")

class LoginFormView(LoginView):
    def post(self, request, id):
        pass

class CallbackView(View):
    def get(self, request):
        token = request.GET.get("token")
        id = request.GET.get("user_id")
        if token and id:
            response = requests.get(f'http://127.0.0.1:8000/authentication/tbd/validate_token/?token={token}&id={id}')
            if response.status_code == 200:
                user, _ = User.objects.get_or_create(username=id, password=id)
                login(request, user)
                return redirect("/userprofile/1")
        return redirect("/login/")