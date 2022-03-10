from django.db import models
import datetime
from accomodation.landlords.models import LandlordProfile
from accomodation.students.models import User, StudentProfile
# Create your models here.
GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Both', 'Both')
]


def directory_path_house(instance, filename, *args):
    # file will be uploaded to MEDIA_ROOT/houses/<landlord>/<address>
    return 'houses/{0}{1}/{2}'.format(instance.User.last_name, instance.House.address, filename)


class House(models.Model):
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, primary_key=True)
    area = models.CharField(max_length=100)
    rent = models.IntegerField(max_length=30)
    gender_required = models.CharField(max_length=30, choices=GENDER)
    distance_from_campus = models.IntegerField(max_length=10)
    description = models.TextField(max_length=1000)
    capacity = models.IntegerField(max_length=10)
    front_image = models.ImageField(upload_to=directory_path_house)
    room1 = models.ImageField(upload_to=directory_path_house)
    room2 = models.ImageField(upload_to=directory_path_house)
    room3 = models.ImageField(upload_to=directory_path_house)
    slug = models.SlugField(upload_to=directory_path_house)

    def __str__(self):
        return self.address


class Booking(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100)
    has_payed = models.BooleanField(default=False)

    def __str__(self):
        #return "{0} {1} has booked at {2} for {3}".format()
        pass
