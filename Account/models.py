from django.db import models
from datetime import datetime as dt
# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=dt.now)
    def __str__(self):
        return self.name + " " + self.email + " " + str(self.comment_date)