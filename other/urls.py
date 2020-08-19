from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about,name='about'),
    path('home_advertise/',views.home_advertise,name='home_advertise'),
    path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
    path('premium_listing/',views.premium_listing,name='premium_listing'),

    # dashboard URLS Part
    path('advertise_us/',views.advertise_us,name='advertise_us'),
]