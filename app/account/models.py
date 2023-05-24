# app/account/models.py

# Django & third party modules
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Locals

# Create your models here.


def get_profile_image_filepath(self, filename):
	"""Defining image path for each user"""
	return 'profile_images/' + str(self.pk) + '/profile_image.png'

def get_default_profile_image():
	"""Defining default image path in case user has no image"""
	return "images/logo_1080_1080.png"


# MODEL:Account
class Account(AbstractBaseUser):
	"""Defining user management in the system"""

	"""Defining user creaentials"""
	email 			= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 		= models.CharField(max_length=30, unique=True)
	date_joined		= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin		= models.BooleanField(default=False)
	is_active		= models.BooleanField(default=True)
	is_staff		= models.BooleanField(default=False)
	is_superuser	= models.BooleanField(default=False)
	profile_image	= models.ImageField(max_length=255, 
						upload_to=get_profile_image_filepath, 
						null=True, 
						blank=True, 
						default=get_default_profile_image)
	# Hiding the user's email from other users
	hide_email		= models.BooleanField(default=True)

	# Email and Username are required to create account
	# User must use its email to login
	USERNAME_FIELD = 'email' # Refer to email in line 26
	REQUIRED_FIELDS = ['username'] # Refer to username in line 27

	def __str__(self):
		return self.username

	# Get profile image of the user from the:get_profile_image_filepath
	def get_profile_image_filename(self):
		return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True