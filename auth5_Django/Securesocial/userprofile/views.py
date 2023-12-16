from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
import requests
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "home_page.html")
# Create your views here.
class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        try:
            user = User.objects.get(username=id)
        except ObjectDoesNotExist:
            return render(request, "user_not_found.html", {'id': id})
        return render(request, "profile_page.html")

class LoginFormView(LoginView):
    def post(self, request, id):
        pass

class CallbackView(View):
    def get(self, request):
        token = request.GET.get("token")
        id = request.GET.get("user_id")
        if token and id:
            response = requests.get(f'https://auth5.pythonanywhere.com/authentication/tbd/validate_token/?token={token}&id={id}')
            if response.status_code == 200:
                user, _ = User.objects.get_or_create(username=id, password=id)
                UserProfile.objects.create(user=user, token=token)
                login(request, user)
                return redirect("/userprofile/"+id)
            print('Invalid token or Id, response returned with status code: ', response.status_code)  
            return render(request, "/login/", {'error': 'something went wrong'})
        print('token or id not specified in callback request', 'token: ', token, 'id: ',id)  
        return render(request, "/login/", {'error': 'something went wrong'})