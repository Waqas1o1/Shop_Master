from django.contrib import admin
from .models import Product,Item,Promotions,TimeDeal,ItemComment
# Register your models here.
admin.site.register((Product,Item,Promotions,TimeDeal,ItemComment))