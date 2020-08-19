from django.shortcuts import render
from columbus import settings

def event_result(request):
    return render(request,'event/event-search-result.html',{"BASE_URL": settings.Base_url})

def event_detail(request):
    return render(request,'event/event-search-detail.html',{"BASE_URL": settings.Base_url})

def post_event(request):
    return render(request,'event/post-event.html',{"BASE_URL": settings.Base_url})

def my_event(request):
    return render(request,'event/my-event.html',{"BASE_URL": settings.Base_url})