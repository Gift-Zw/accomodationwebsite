from django.urls import path
from .views import StudentBookingsListView

app_name = 'students'

urlpatterns = [
    path('bookings/', StudentBookingsListView.as_view(), name="student-bookings")
]