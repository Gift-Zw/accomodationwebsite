from django.db import models
from students.models import User
# Create your models here.


class LandlordProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cell = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
