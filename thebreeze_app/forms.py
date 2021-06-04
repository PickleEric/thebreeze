from django import forms
from .models import Resturant

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class ResturantForm(forms.ModelForm):
    class Meta:
        model = Resturant
        fields = ['name', 'direction', 'hyper_link', 'hours_open', 'description']