from django.db import models
from accomodation.students.models import User
# Create your models here.


class LandlordProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE())
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cell = models.CharField(max_length=20)
