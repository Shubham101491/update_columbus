from django.shortcuts import render
from columbus import settings

def travel_result(request):
    return render(request,'travel/travel-search-result.html',{"BASE_URL": settings.Base_url})

def travel_detail(request):
    return render(request,'travel/travel-search-detail.html',{"BASE_URL": settings.Base_url})