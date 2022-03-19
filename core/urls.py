from django.urls import path
from .views import HouseListView, HouseDetailView, HomeView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('house-list/', HouseListView.as_view(), name="house-list"),
    path('house-detail/', HouseDetailView.as_view(), name="house-detail"),
]