# app/account/admin.py

# Django & third party modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Locals
from app.account.models import Account

# Defining the look of Account table in admin panel
class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined','last_login','is_admin','is_staff')
	search_fields = ('email','username')
	readonly_fields = ('id','date_joined','last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

# Register your models here.

admin.site.register(Account, AccountAdmin)