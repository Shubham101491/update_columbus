from django.urls import path
from . import views

urlpatterns = [
    path('hotel_result/',views.hotel_result,name='hotel_result'),
    path('hotel_detail/',views.hotel_detail,name='hotel_detail'),
    path('post_hotel/',views.post_hotel,name='post_hotel'),
    path('my_hotel/',views.my_hotel,name='my_hotel'),
    path('preview/',views.preview,name='preview'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]