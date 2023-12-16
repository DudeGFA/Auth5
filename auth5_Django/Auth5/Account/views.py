from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import LogoutSerializer, RegistrationSerializer
from django.views import View
from django.shortcuts import  render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import NewUserForm, WebsiteForm, UrlForm, NewWebsiteUserForm
import uuid, secrets
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from Account.models import Field, FieldGroup, UserProfile, WebsiteAccount, Website
from django.contrib.auth.forms import UserCreationForm

class LoginFormView(LoginView):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        if username and password:
            user = authenticate(request, username=username.strip(), password=password.strip())
            if user is not None:
                try:
                    if not user.profile:
                        return render(request, 'registration/login.html', {'errors':'Incorrect Login credentials'})
                except Exception:
                    return render(request, 'registration/login.html', {'errors':'Incorrect Login credentials'})
                login(request, user)
                print("successful authentication")
                return redirect("/dashboard")
        return render(request, "registration/login.html")

class WebsiteLoginFormView(View):
    def get(self, request):
        return render(request, 'website/login.html')
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        if username and password:
            user = authenticate(request, username=username.strip(), password=password.strip())
            try:
                if user is not None and user.website:
                    login(request, user)
                    print("successful authentication")
                    return redirect("/dashboard/website")
            except Exception:
                pass
        ctx = {'errors':{'Authentication error':'Incorrect Login credentials'}}
        return render(request, "website/login.html", ctx)

class RegistrationFormView(View):

    def get(self, request):
        website_name = request.GET.get("website")
        print(website_name, 'get')
        if website_name:
            return render(request, 'authentication/register.html', {'website_name': website_name})
        return render(request, 'register.html')

    def create_fields(self, new_user):
        new_field_group = FieldGroup.objects.create(name='default_field_group', owner=new_user.profile)
        image_field = Field.objects.create(name="profile_picture", group=new_field_group)
        first_name_field = Field.objects.create(name="first_name", group=new_field_group)
        last_name_field = Field.objects.create(name="last_name", group=new_field_group)
        middle_name_field = Field.objects.create(name="middle_name", group=new_field_group)
        dob_field = Field.objects.create(name="date_of_birth", group=new_field_group)
        Address = Field.objects.create(name="address", group=new_field_group)
        phone = Field.objects.create(name="phone_number", group=new_field_group)
        occupation = Field.objects.create(name="occupation", group=new_field_group)

    def post(self, request):
        random_password = secrets.token_urlsafe(16)
        website_name = request.POST.get("website_name")
        print(website_name, 'post')
        while (True):
            try:
                user_id = uuid.uuid4()
                newform = NewUserForm({'username': user_id, 'password1': random_password, 'password2': random_password, 'email':'auth5user@gmail.com'})
                if newform.is_valid():
                    new_user = newform.save()
                    new_user_profile = UserProfile.objects.create(user=new_user)
                    self.create_fields(new_user)
                    login(request, new_user)
                    context = {'username': user_id, 'password': random_password}
                    if (website_name):
                        context['website_name'] = website_name
                        return render(request, 'authentication/register_success.html', context)
                    return render(request, 'signup_success.html', context)
                else:
                    print(newform.errors)
            except IntegrityError:
                pass
        return render(request, 'signup_success.html')

class WebsiteRegistrationFormView(View):

    def get(self, request):
        return render(request, 'website/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        link = request.POST.get('link')
        try:
            newform = NewWebsiteUserForm({'username': username, 'password1': password, 'password2': password, 'email': email})
            url_form = UrlForm({'url': link})
            if newform.is_valid() and url_form.is_valid():
                new_user = newform.save()
                new_website = WebsiteForm({'user': new_user, 'link': link})
                if new_website.is_valid():
                    new_website.save()
                    login(request, new_user)
                    context = {}
                    return redirect('/dashboard/website')
                else:
                    print(new_website.errors)
            else:
                print(newform.errors)
        except IntegrityError:
            pass
        return render(request, 'website/register.html', {'user_form_errors': newform.errors, 'url_form_errors': url_form.errors})


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class LoginRefreshView(TokenRefreshView):
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "You have logged out successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )