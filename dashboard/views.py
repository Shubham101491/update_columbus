from django.shortcuts import render
from columbus import settings

def dashboard(request):
    return render(request,'dashboard/dashboard.html',{"BASE_URL": settings.Base_url})
    