from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Account.models import FieldGroup, Field
from django import forms
# Create your forms here.

class GroupForm(forms.ModelForm):
	class Meta:
		model = FieldGroup
		fields = ("name", "owner")

class FieldForm(forms.ModelForm):
	class Meta:
		model = Field
		fields = ("did", "recordid", "name", "group")