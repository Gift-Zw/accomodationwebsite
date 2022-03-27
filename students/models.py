from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female')
]


class User(AbstractUser):
    username = models.CharField(max_length=100, primary_key=True)
    is_student = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)
    is_basic = models.BooleanField(default=False)
    is_standard = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)
    cell = models.CharField(max_length=20)
    level = models.DecimalField(decimal_places=1, max_digits=3)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

