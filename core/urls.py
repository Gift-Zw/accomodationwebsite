from django.urls import path
from .views import HouseListView, HouseDetailView, HomeView, contact_view

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('house-list/', HouseListView.as_view(), name="house-list"),
    path('contact/', contact_view, name="contact"),
]