from django.urls import path
from .views import LandlordPortalView, confirm_payment
app_name = 'landlords'

urlpatterns = [
    path('bookings/', LandlordPortalView.as_view(), name='bookings'),
    path('confirm-payment/', confirm_payment, name='confirm-payment')
]