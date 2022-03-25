from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import House, Booking
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accomodation.decorators import student_required, landlord_required
from django.contrib import messages

# Create your views here.


@method_decorator(login_required, name='dispatch')
class HouseListView(ListView):
    template_name = 'houselist.html'
    model = House
    paginate_by = 3
    extra_context = {'list': "active"}


@method_decorator(login_required, name='dispatch')
class HouseDetailView(DetailView):
    model = House
    template_name = 'housedetail.html'
    houses = House.objects.all()
    extra_context = {'houses':houses}


class HomeView(ListView):
    template_name = 'home.html'
    model = House
    extra_context = {'home': "active"}


def contact_view(request):
    context = {
        'contact':'active'
    }
    return render(request, template_name='contact.html', context=context)


@student_required
def book_house(request, slug):
    house = get_object_or_404(House, slug=slug)

    order_query = Booking.objects.filter(student=request.user, house=house)
    if order_query.exists():
        messages.info(request, 'You have already booked this house.')
        return redirect("core:house-list")
    else:
        booking = Booking.objects.create(
            student=request.user,
            house=house,
            duration="1 month",
            landlord=house.landlord
        )
        booking.save()
        messages.success(request, 'You have successfully booked this house.')
        return redirect("core:house-list")


@landlord_required
def landlord_delete_booking(request, id):
    booking = Booking.objects.filter(id=id)
    booking.delete()
    messages.info(request, 'You have successfully deleted the booking')
    return redirect("landlords:bookings")


@student_required
def student_delete_booking(request, id):
    booking = Booking.objects.filter(id=id)
    booking.delete()
    messages.info(request, 'You have successfully deleted the booking')
    return redirect("students:student-bookings")

