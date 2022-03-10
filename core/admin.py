from django.contrib import admin
from models import Booking, House
# Register your models here.


class HouseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': 'address'}


admin.register(House, HouseAdmin)
admin.register(Booking)