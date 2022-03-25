from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, ListView
from .forms import StudentSignUpForm, CreateStudentForm, StudentProfileForm
from .models import User
from core.models import Booking
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accomodation.decorators import student_required, landlord_required


# Create your views here.

def register_page(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        profile_form = StudentProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.is_student = True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request,  'Your account has been successfully created')
            return redirect('/')

    else:
        form = CreateStudentForm()
        profile_form = StudentProfileForm()

        context = {'form': form,
                   'profile_form': profile_form}
        return render(request, 'students/signup.html', context)


@method_decorator([login_required, student_required], name='dispatch')
class StudentBookingsListView(ListView):
    template_name = 'students/dashboard.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        self.user = get_object_or_404(User, name=self.kwargs['user'])
        return Booking.objects.filter(user=self.user)


@student_required
def student_dash(request):
    bookings = Booking.objects.filter(student=request.user)
    context = {
        'bookings':bookings,
        'dash': 'active'
    }
    return render(request, template_name='students/dashboard.html', context=context)