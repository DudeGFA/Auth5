from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Website

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "password1")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.username = self.cleaned_data['username']
		if commit:
			user.save()
		return user

class NewWebsiteUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "password1", "email")

	def save(self, commit=True):
		user = super(NewWebsiteUserForm, self).save(commit=False)
		user.username = self.cleaned_data['username']
		if commit:
			user.save()
		return user

class WebsiteForm(forms.ModelForm):
	class Meta:
		model = Website
		fields = ("link", "user")

class UrlForm(forms.Form):
    url = forms.URLField(label='Enter a URL')