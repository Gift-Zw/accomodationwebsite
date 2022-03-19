"""accomodation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from students.views import StudentSignUpView
from landlords.views import LandlordSignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('student/', include('core.urls', namespace='students')),
    path('landlord/', include('core.urls', namespace='landlords')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='students-signup'),
    path('accounts/signup/landlord/', LandlordSignUpView.as_view(), name='landlord-signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)