from django.shortcuts import render
from columbus import settings

def homestay_result(request):
    return render(request,'homestay/homestay-search-result.html',{"BASE_URL": settings.Base_url})

def homestay_detail(request):
    return render(request,'homestay/homestay-search-detail.html',{"BASE_URL": settings.Base_url})

def post_homestay(request):
    return render(request,'homestay/post-homestay.html',{"BASE_URL": settings.Base_url})

def my_homestay(request):
    return render(request,'homestay/my-homestay.html',{"BASE_URL": settings.Base_url})
