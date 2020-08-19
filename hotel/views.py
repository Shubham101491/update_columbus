from django.shortcuts import render
from columbus import settings

def hotel_result(request):
    return render(request,'hotel/hotel-search-result.html',{"BASE_URL": settings.Base_url})

def hotel_detail(request):
    return render(request,'hotel/hotel-search-detail.html',{"BASE_URL": settings.Base_url})

def post_hotel(request):
    return render(request,'hotel/post-hotel.html',{"BASE_URL": settings.Base_url})

def my_hotel(request):
    return render(request,'hotel/my-hotel.html',{"BASE_URL": settings.Base_url})
