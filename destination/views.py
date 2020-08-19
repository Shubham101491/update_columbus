from django.shortcuts import render
from columbus import settings

def destination_result(request):
    return render(request,'destination/destination-search-result.html',{"BASE_URL": settings.Base_url})

def destination_detail(request):
    return render(request,'destination/destination-detail.html',{"BASE_URL": settings.Base_url})