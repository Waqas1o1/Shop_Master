from django.urls import path
from .import views
urlpatterns = [
    path('',views.Index,name='blogpage'),
    path('Blog/<int:bid>',views.BlogPost,name='blogpage'),
    path('blogcomment/<int:bid>',views.Blogcomment,name='blogpage'),
]