from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import secrets, uuid
from django.contrib.auth.models import User
from Account.models import Website, WebsiteAccount, FieldGroup
from django.views import View
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from Account.models import WebsiteAccount
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

class ValidateTokenView(View):
    def get(self, request, website_name):
        token = request.GET.get("token")
        id = request.GET.get("id")
        get_object_or_404(WebsiteAccount, validation_token=token, website__user__username=website_name.strip(), user_id_on_website=id)
        return HttpResponse({'message':'valid token'}, status=200)

class AuthenticateView(View):
    def update_or_create_website_account(self, user, website, validation_token):
        # Define the conditions to find a WebsiteAccount
        conditions = {
            'user_profile': user.profile,
            'website': website,
        }

        # Define the data to update or create
        defaults = {
            'validation_token': validation_token,
        }

        # Get or create a WebsiteAccount based on the conditions
        website_account, created = WebsiteAccount.objects.update_or_create(
            **conditions,
            defaults=defaults
        )
        if (created):
            field_group = FieldGroup.objects.filter(name='default_field_group',owner=user.profile).first()
            while (True):
                user_id = uuid.uuid4()
                try:
                    existing_account = WebsiteAccount.objects.get(user_id_on_website=user_id)
                except ObjectDoesNotExist:
                    # No existing account found with this user_id, safe to update
                    website_account.user_id_on_website = user_id
                    website_account.field_group = field_group
                    website_account.save()
                    break
        return website_account.user_id_on_website

    def get(self, request, website_name):
        website = Website.objects.filter(user__username=website_name).first()
        if (website):
            ctx = {'website_name': website_name}
            return render(request, 'authentication/login.html', ctx)
        else:
            print(website)
            ctx = {'error': 'Website with name '+website_name+" isn't registered with Auth5"}
            return render(request, 'authentication/error.html', ctx)

    def post(self, request, website_name):
        # Implement your authentication logic here
        # On successful login, generate a secure token
        website = Website.objects.filter(user__username=website_name).first()
        if (not website):
            return render(request, 'authentication/error.html')
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            # Generate a secure token
            token = secrets.token_urlsafe(32)
            # Redirect to XYZ.com's callback URL with the token
            if (website.callback_url):
                callback_url = website.callback_url
            else:
                callback_url = request.POST.get("referring_url")
            print(callback_url)
            if callback_url:
                callback_url =  callback_url.strip()
                token, created = Token.objects.get_or_create(user=user)
                if callback_url[-1] != '/':
                    callback_url += '/'
                user_id_on_website = self.update_or_create_website_account(user, website, token.key)
                return redirect(f'{callback_url}?token={token.key}&user_id={user_id_on_website}')
            else:
                return render(request, 'authentication/error.html', {'error_message': 'No Call back url specified'})
        else:
            # Handle unsuccessful login
            ctx = {'error_message': 'Invalid credentials', 'website_name': website_name, 'referring_url': request.POST.get("referring_url")}
            return render(request, 'authentication/login.html', ctx)
