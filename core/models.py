from django.db import models
from accomodation.landlords.models import LandlordProfile
from accomodation.students.models import User, StudentProfile
# Create your models here.


class House(models.Model):
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE())
    number_and_street = models.CharField(max_length=100, primary_key=True)
    area = models.CharField(max_length=100)
    rent = models.IntegerField(max_length=30)
    gender_required = models.Choices()
    distance_from_campus = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    capacity = models.IntegerField(max_length=10)
    front_image = models.ImageField()
    room1 = models.ImageField()
    room2 = models.ImageField()
    room3 = models.ImageField()


class Bookings(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    house = models.OneToOneField(House, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100)
    has_payed = models.BooleanField(default=False)

