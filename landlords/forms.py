from django import forms
from students.models import User
from .models import LandlordProfile
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm


class LandlordSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    cell = forms.CharField(max_length=20, initial="+263")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'cell', 'email', 'password1', 'password2')


class CreateLandlordForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LandlordProfileForm(forms.ModelForm):
    class Meta:
        model = LandlordProfile
        fields = ['first_name', 'last_name', 'cell']
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "cell": "Cell",
        }