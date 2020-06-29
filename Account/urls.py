
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.Index,name='indexlogin'),
    path('login/',views.Login_Handle,name='login_handle'),
    path('log_out/',views.Log_out,name='logout_handle'),
    path('register/',views.SiginUp_Handle,name='SiginUp'),
    path('contact_us/',views.Contact_Us,name='contact_us'),

]

