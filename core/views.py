from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import House


# Create your views here.


class HouseListView(ListView):
    template_name = 'houselist.html'
    queryset = House.objects.all()
    context_object_name = 'books'
    paginate_by = 8

    """ To be used we want to view houses by certain attribs
        def get_queryset(self):
        return House.objects.filter(created_by=self.request.user)
    """


class HouseDetailView(ListView):
    model = House
    template_name = 'housedetail.html'


class HomeView(ListView):
    template_name = 'home.html'
    queryset = House.objects.all()
    context_object_name = 'house'