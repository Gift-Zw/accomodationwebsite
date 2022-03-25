from django.urls import path
from .views import StudentBookingsListView, student_dash

app_name = 'students'

urlpatterns = [
    path('bookings/', student_dash, name="student-bookings")
]