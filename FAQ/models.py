from django.db import models

# Create your models here.
class FAQ(models.Model):
    Question = models.CharField(max_length=200);
    Answer = models.TextField()
    Answer2 = models.TextField(blank=True)
    def __str__(self):
        return str(self.id) + ' :  ' + self.Question