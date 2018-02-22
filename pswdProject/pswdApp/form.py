from django import forms
from django.db import models
from django.contrib.auth.models import User
from pswdApp.models import UserProfileInfo

class UserForm(forms.ModelForm):

	userPswd = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username','email','userPswd')

class UserProfileInfoForm(forms.ModelForm):

	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site','profile_pic')