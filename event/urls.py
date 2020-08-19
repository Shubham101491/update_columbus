from django.urls import path
from . import views

urlpatterns = [
    path('event_result/',views.event_result,name='event_result'),
    path('event_detail/',views.event_detail,name='event_detail'),
    path('post_event/',views.post_event,name='post_event'),
    path('my_event/',views.my_event,name='my_event'),
]