from django.urls import path
from . import views

urlpatterns = [
    path('travel_result/',views.travel_result,name='travel_result'),
    path('travel_detail/',views.travel_detail,name='travel_detail'),
]