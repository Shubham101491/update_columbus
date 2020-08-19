from django.shortcuts import render
from columbus import settings

def about(request):
    return render(request,'other/about.html',{"BASE_URL": settings.Base_url})

def home_advertise(request):
    return render(request,'other/home-advertise-us.html',{"BASE_URL": settings.Base_url})

def privacy_policy(request):
    return render(request,'other/privacy-policy.html',{"BASE_URL": settings.Base_url})

def advertise_us(request):
    return render(request,'other/advertise-us.html',{"BASE_URL": settings.Base_url})

def premium_listing(request):
    return render(request,'other/premium-listing.html',{"BASE_URL": settings.Base_url})