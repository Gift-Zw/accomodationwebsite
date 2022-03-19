from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import House
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(login_required, name='dispatch')
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


def contact_view(request):
    context = {}
    return render(request, template_name='contact.html', context=context)