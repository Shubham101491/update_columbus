from django.urls import path
from . import views

urlpatterns = [
    path('homestay_result/',views.homestay_result,name='homestay_result'),
    path('homestay_detail/',views.homestay_detail,name='homestay_detail'),
    path('post_homestay/',views.post_homestay,name='post_homestay'),
    path('my_homestay/',views.my_homestay,name='my_homestay'),
]