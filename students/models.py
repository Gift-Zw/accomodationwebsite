from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER = [
    ('M', 'Male'),
    ('F', 'Female')
]


class User(AbstractUser):
    email = models.EmailField(primary_key=True)
    is_student = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER)
    cell = models.CharField(max_length=20)
    level = models.IntegerField(max_length=10)