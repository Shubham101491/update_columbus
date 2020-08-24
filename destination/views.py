from django.shortcuts import render, get_object_or_404
from columbus import settings

# use models
from destination.models import dest_detail
from destination.models import dest_video
from destination.models import dest_photo

def destination_result(request):
    location = dest_detail.objects.all()
    return render(request,'destination/destination-search-result.html',{"BASE_URL": settings.Base_url,'locations':location})

def destination_detail(request):
    dest_data = None
    get_video = None
    get_photo = None
    if dest_detail.objects.filter().exists():
        dest_data = get_object_or_404(
            dest_detail)
    if dest_video.objects.filter(dest_detail=dest_data).exists():
        get_video = dest_video.objects.filter(
            dest_detail=dest_data)
    if dest_photo.objects.filter(dest_detail=dest_data).exists():
        get_photo = dest_photo.objects.filter(
            dest_detail=dest_data)
    return render(request,'destination/destination-detail.html',{"BASE_URL": settings.Base_url,'dest_data': dest_data, 'get_video': get_video, 'pic': get_photo})