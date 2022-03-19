from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import CreateView, ListView
from .forms import LandlordProfile
from students.models import User
from core.models import Booking

# Create your views here.


class LandlordSignUpView(CreateView):
    model = User
    form_class = LandlordProfile
    template_name = 'landsignup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'landlord'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class LandlordPortalView(ListView):
    template_name = ''
    queryset = Booking.objects.filter()
    context_object_name = 'booking'


def confirm_payment(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.confirm_payment()
    booking.save()
