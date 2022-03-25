from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import CreateView, ListView
from .forms import CreateLandlordForm, LandlordSignUpForm, LandlordProfileForm
from students.models import User
from core.models import Booking, House
from django.contrib import messages
from accomodation.decorators import landlord_required

# Create your views here.


def landlord_register_page(request):
    if request.method == 'POST':
        form = CreateLandlordForm(request.POST)
        profile_form = LandlordProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.is_landlord = True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request,  'Your account has been successfully created')
            return redirect('/')

    else:
        form = CreateLandlordForm()
        profile_form = LandlordProfileForm()

        context = {'form': form,
                   'profile_form': profile_form}
        return render(request, 'landlords/signup.html', context)


@landlord_required
def landlord_dash(request):
    bookings = Booking.objects.filter(landlord=request.user)
    context = {
        'bookings':bookings,
        'dash': 'active'
    }
    return render(request, template_name='landlords/dashboard.html', context=context)


@landlord_required
def confirm_payment(request, id):
    booking = Booking.objects.get(id=id)
    booking.has_payed = True
    booking.save()
    messages.info(request, 'You have successfully confirmed payment for the booking')
    return redirect("landlords:bookings")
