from django.shortcuts import render,redirect
from columbus import settings
from hotel.forms import HotelForm
from hotel.models import hotels_data

def hotel_result(request):
    return render(request,'hotel/hotel-search-result.html',{"BASE_URL": settings.Base_url})

def hotel_detail(request):
    return render(request,'hotel/hotel-search-detail.html',{"BASE_URL": settings.Base_url})

def post_hotel(request):
    if request.method == "POST":
        form = HotelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('http://127.0.0.1:8000/hotel/preview/')
            except:
                pass
    else:
        form = HotelForm()
        return render(request,'hotel/post-hotel.html',{"BASE_URL": settings.Base_url,'form':form})

def preview(request):
    hotel = hotels_data.objects.all()
    return render(request,'hotel/hotel-preview.html',{"BASE_URL": settings.Base_url,'hotel':hotel})

def my_hotel(request):
    hotel = hotels_data.objects.all()
    return render(request,'hotel/my-hotel.html',{"BASE_URL": settings.Base_url,'hotel':hotel})

def edit(request,id):
    hotel = hotels_data.objects.get(id=id)
    return render(request,'hotel/edit-post-hotel.html',{"BASE_URL": settings.Base_url,'hotel':hotel})

def update(request,id):
    hotel = hotels_data.objects.get(id=id)
    form = HotelForm(request.POST,instance = hotel)
    if form.is_valid():
        form.save()
        return redirect("http://127.0.0.1:8000/hotel/my_hotel")
    return render(request,'hotel/edit-post-hotel.html',{"BASE_URL": settings.Base_url,'hotel':hotel})

def delete(request,id):
    hotel = hotels_data.objects.get(id=id)
    hotel.delete()
    return redirect("http://127.0.0.1:8000/hotel/my_hotel")