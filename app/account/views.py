# app/account/views.py

# Django & third parties modules 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

# Locals
from app.account.forms import RegistrationForm

# Create your views here.

def register_view(request, *args, **kwargs):

	"""Remain the authenticated user (already logged in user), 
	if he/she try to access the register form with the HttpResponse text
	that is 'You are already authenticated as {user.email}.' """
	user = request.user 
	if user.is_authenticated:
		return HttpResponse(f"You are already authenticated as {user.email}.")
	context = {}

	# If register form is submited
	if request.POST:

		# Get all the paramters form the register form fields
		form = RegistrationForm(request.POST)
		
		# Create the user an account (save the parameters)
		# if all parameters (form) is valid
		if form.is_valid():
			form.save()

			# Because account has been created, login the user
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email,password=raw_password)
			login(request,account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect("personal:home")

		# If form is not valid, return the form
		else:
			context['registration_form'] = form 

	return render(request, 'account/register.html', context)