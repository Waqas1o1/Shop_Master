from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from datetime import datetime as dt
# Create your models here.
class Blog_Post(models.Model):
    title = models.CharField(max_length=400) 
    Paragraph = HTMLField()
    blog_auther = models.CharField(max_length=300,default='')
    auther_bio = models.CharField(max_length=300,default='')
    auther_thumbnail = models.ImageField(default='')
    cover_img  = models.ImageField(default='')
    img_1 = models.ImageField(blank=True) 
    img_2 = models.ImageField(blank=True)
    img_3 = models.ImageField(blank=True)
    img_4 = models.ImageField(blank=True)
    img_5 = models.ImageField(blank=True)
    img_6 = models.ImageField(blank=True)
    blog_quote_1 = models.CharField(max_length=300,blank=True)
    blog_quote_2 = models.CharField(max_length=300,blank=True)
    publish_date = models.DateTimeField(default=dt.now())
    tags = TaggableManager()
    def __str__(self):
        return self.title 
class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post =  models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now_add=dt.now)
    def __str__(self):
        return self.comment[:20] + ' : ' + str(self.user)