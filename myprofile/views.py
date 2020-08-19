from django.shortcuts import render
from columbus import settings

def profile(request):
    return render(request,'profile/profile.html',{"BASE_URL": settings.Base_url})