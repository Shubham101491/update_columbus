from django.urls import path
from . import views

urlpatterns = [
    path('registerpost/',views.registerpost,name='registerpost'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('login_otp/<slug:user_code>',views.login_otp,name='login_otp'),
]