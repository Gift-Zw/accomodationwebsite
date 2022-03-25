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

LOCATIONS = [
    ('Selborne Park 1', 'Selborne Park 1'),
    ('Selborne Park 2', 'Selborne Park 2'),
    ('Parklands', 'Parklands'),
    ('Khumalo', 'Khumalo'),
    ('Riverside', 'Riverside'),
    ('Sunminghill', 'Sunminghill'),
    ('Woodlands', 'Woodlands'),
    ('Matsheomuhlope', 'Matsheomuhlope')

]

def directory_path_house(instance, filename, *args):
    # file will be uploaded to MEDIA_ROOT/houses/<landlord>/<address>
    return 'houses/{0}/{1}/{2}'.format(instance.landlord.last_name, instance.address, filename)


class House(models.Model):
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, default='ME')
    address = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=100, choices=LOCATIONS)
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
        return reverse('core:house-detail', kwargs={
            'slug': self.slug
        })

    def get_book_house(self):
        return reverse('core:book-house', kwargs={
            'slug': self.slug
        })

    def get_remove_booking(self):
        return reverse('core:house-detail', kwargs={
            'slug': self.slug
        })


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name='landlord')
    duration = models.CharField(max_length=100)
    has_payed = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    def confirm_payment(self):
        return reverse('landlords:confirm-payment', kwargs={
            'id': self.id,
        })

    def landlord_delete_booking(self):
        return reverse('core:landlord-delete-booking', kwargs={
            'id': self.id,

        })

    def student_delete_booking(self):
        return reverse('core:student-delete-booking', kwargs={
            'id': self.id,
        })

    def __str__(self):
        return f"{self.student.studentprofile.first_name} {self.student.studentprofile.last_name} has booked {self.house.address} for {self.duration}"

