from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import LandlordProfile
from ..students.models import User

# Create your views here.


class LandlordSignUpView(CreateView):
    model = User
    form_class = LandlordProfile
    template_name = ''

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'landlord'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('#url of landlord portal')