from django.db import models
from django.urls import reverse
from landlords.models import LandlordProfile
from students.models import User, StudentProfile
# Create your models here.
GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Both', 'Both')
]


def directory_path_house(instance, filename, *args):
    # file will be uploaded to MEDIA_ROOT/houses/<landlord>/<address>
    return 'houses/{0}/{1}/{2}'.format(instance.landlord.last_name, instance.address, filename)


class House(models.Model):
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, primary_key=True)
    area = models.CharField(max_length=100)
    rent = models.IntegerField()
    gender_required = models.CharField(max_length=30, choices=GENDER)
    distance_from_campus = models.DecimalField(decimal_places=1, max_digits=6)
    description = models.TextField(max_length=1000)
    capacity = models.IntegerField()
    front_image = models.ImageField(upload_to=directory_path_house)
    room1 = models.ImageField(upload_to=directory_path_house)
    room2 = models.ImageField(upload_to=directory_path_house)
    room3 = models.ImageField(upload_to=directory_path_house)
    slug = models.SlugField()
    date_uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('core:#name of view', kwargs={
            'slug': self.slug
        })

    def get_book_house(self):
        return reverse('core:#name of view', kwargs={
            'slug': self.slug
        })

    def get_remove_booking(self):
        return reverse('core:#name of view', kwargs={
            'slug': self.slug
        })


class Booking(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100)
    has_payed = models.BooleanField(default=False)

    def confirm_payment(self):
        self.has_payed = True

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} has booked {self.house.address} for {self.duration}"

