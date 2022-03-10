from django.db import models

# Create your models here.


class House(models.Model):
    #landlord =
    number_and_street = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    rent = models.IntegerField(max_length=30)
    gender = models.Choices()
    distance_from_campus = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    capacity = models.IntegerField(max_length=10)
    front_image = models.ImageField()
    room1 = models.ImageField()
    room2 = models.ImageField()
    room3 = models.ImageField()


class Bookings(models.Model):
    pass