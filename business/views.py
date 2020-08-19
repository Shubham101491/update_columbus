from django.shortcuts import render
from columbus import settings

def list_business(request):
    return render(request,'business/list-business.html',{"BASE_URL": settings.Base_url})

def my_business(request):
    return render(request,'business/my-business.html',{"BASE_URL": settings.Base_url})
