from django.urls import path
from views import StudentBookingsListView, StudentSignUpView

app_name = 'students'

urlpatterns = [
    path('signup/', StudentSignUpView.as_view(),name="student-signup"),
    path('bookings/', StudentBookingsListView.as_view(), name="student-bookings")
]