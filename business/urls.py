from django.urls import path
from . import views

urlpatterns = [
    path('list_business/',views.list_business,name='list_business'),
    path('my_business/',views.my_business,name='my_business'),
]