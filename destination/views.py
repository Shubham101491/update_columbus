from django.shortcuts import render
from columbus import settings

# use models
from destination.models import city
from destination.models import dest_detail
from destination.models import dest_video
from destination.models import dest_photo

def destination_result(request):
    location = dest_detail.objects.all()
    return render(request,'destination/destination-search-result.html',{"BASE_URL": settings.Base_url,'locations':location})

def destination_detail(request):
    location = dest_detail.objects.all()
    return render(request,'destination/destination-detail.html',{"BASE_URL": settings.Base_url,'locations':location})