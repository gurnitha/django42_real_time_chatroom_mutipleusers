# app/account/forms.py

# Django & third parties modules 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from app.account.models import Account


class RegistrationForm(UserCreationForm):

	# Add email field to the form (by default UserCreationForm has no email field)
	email = forms.EmailField(
			max_length=254, 
			help_text='Required. Add a valid email address.')

	# Use Account models fields and fields in the UserCreationForm in the form
	class Meta:
		model = Account
		fields = ('email', 'username', 'password1', 'password2')

	# Check and clean the emsil if user submit the form
	def clean_email(self):
		# Get email from the form input with attribute name="email"
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.get(email=email)
		except Exception as e:
			return email
			
		raise forms.ValidationError(f"Email {email} is already in use.")

	# Check and clean the username if user submit the form
	def clean_username(self):
		# Get username from the form input with attribute name="username"
		username = self.cleaned_data['username']
		try:
			account = Account.objects.get(username=username)
		except Exception as e:
			return username

		raise forms.ValidationError(f"Username {username} is already in use.")

