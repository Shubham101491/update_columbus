from django.urls import path
from . import views

urlpatterns = [
    path('destination_result/',views.destination_result,name='destination_result'),
    path('destination_detail/',views.destination_detail,name='destination_detail'),
]