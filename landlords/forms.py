from django import forms
from accomodation.students.models import User
from models import LandlordProfile
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm


class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    cell = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_landlord = True
        user.save()
        landlord = LandlordProfile.objects.create(
            user=user,
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            cell=self.cleaned_data.get('cell'),
        )
        landlord.save()
        return user