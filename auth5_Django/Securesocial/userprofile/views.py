from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView

# Create your views here.
class UserProfileView(View):
    def get(self, request, id):
        return render(request, "profile_page.html")

class LoginFormView(LoginView):
    def post(self, request, id):
        pass