from django.contrib import admin
from .models import Blog_Post,BlogComment
# Register your models here.
admin.site.register((Blog_Post,BlogComment))