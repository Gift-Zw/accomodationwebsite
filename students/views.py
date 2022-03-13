from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, ListView
from .forms import StudentProfile
from .models import User
from core.models import Booking


# Create your views here.


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentProfile
    template_name = ''

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('#url of homepage')


class StudentBookingsListView(ListView):
    template_name = ''
    queryset = Booking.objects.filter()
    context_object_name = 'booking'