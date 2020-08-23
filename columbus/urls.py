"""columbus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

# For Media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls','home'),namespace='home')),
    path('destination/', include(('destination.urls','destination'),namespace='destination')),
    path('hotel/', include(('hotel.urls','hotel'),namespace='hotel')),
    path('homestay/', include(('homestay.urls','homestay'),namespace='homestay')),
    path('event/', include(('event.urls','event'),namespace='event')),
    path('tour/', include(('tour.urls','travel'),namespace='tour')),
    path('contact/', include(('contact.urls','contact'),namespace='contact')),
    path('other/', include(('other.urls','other'),namespace='other')),
    path('account/', include(('account.urls','account'),namespace='account')),
    path('dashboard/', include(('dashboard.urls','dashboard'),namespace='dashboard')),
    path('business/', include(('business.urls','business'),namespace='business')),
    path('myprofile/', include(('myprofile.urls','business'),namespace='myprofile')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)