from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import RegularUserChangeForm, RegularUserCreationForm
from .models import RegularUser

# Register your models here.
class RegularUserAdmin(UserAdmin):
    add_form = RegularUserCreationForm
    form = RegularUserChangeForm
    model = RegularUser
    list_display = ["username", "sex", "postal_code", "email"]

admin.site.register(RegularUser, RegularUserAdmin)