from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import StudentProfile, User

# Make forms below.
GENDER = [
    ('Male', 'M'),
    ('Female', 'F')
]


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=GENDER)
    cell = forms.CharField(max_length=20)
    level = forms.IntegerField(max_value=1000)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = StudentProfile.objects.create(
            user=user,
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            gender=self.cleaned_data.get('gender'),
            cell=self.cleaned_data.get('cell'),
            level=self.cleaned_data.get('level')
                                                )
        student.save()
        return user

