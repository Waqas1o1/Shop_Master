from django.shortcuts import render
from .models import FAQ
# Create your views here.
def Index(request):
    faq = FAQ.objects.all()
    send = {'QA':faq}
    return render(request,'faq/faq.html',send)