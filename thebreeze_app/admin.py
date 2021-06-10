from django.contrib import admin

# Register your models here.

from .models import Resturant, Profile

admin.site.register(Resturant)
admin.site.register(Profile)