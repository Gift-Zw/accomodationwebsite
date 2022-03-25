from django.urls import path
from .views import landlord_dash, confirm_payment
app_name = 'landlords'

urlpatterns = [
    path('bookings/', landlord_dash, name='bookings'),
    path('confirm-payment/<id>/', confirm_payment, name='confirm-payment'),

]