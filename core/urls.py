from django.urls import path
from .views import HouseListView,\
    HouseDetailView, HomeView, contact_view, book_house, student_delete_booking, landlord_delete_booking

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('house-list/', HouseListView.as_view(), name="house-list"),
    path('contact/', contact_view, name="contact"),
    path('house/<slug>/', HouseDetailView.as_view(), name='house-detail'),
    path('book-house/<slug>/', book_house, name='book-house'),
    path('landlord-delete-booking/<id>/', landlord_delete_booking, name='landlord-delete-booking'),
    path('student-delete-booking/<id>/', student_delete_booking, name='student-delete-booking'),
]