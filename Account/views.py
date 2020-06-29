from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import ContactUs
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import re 
from django.db import IntegrityError
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
# Create your views here.
def Index(request):
    return render(request,'account/login.html')
def Log_out(request):
    logout(request)
    return redirect('indexlogin')

def Login_Handle(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=user,password=password)
        if u is not None:
            login(request,u)
            messages.add_message(request,messages.INFO,'Login Sucess Welcome :' +str(user).title())
            return redirect('HomePage')
        else:
            messages.add_message(request,messages.ERROR,"Login cridential's is wrong")
    return redirect('indexlogin')
def SiginUp_Handle(request):

    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conform_pass = request.POST['conformpassword']
        error = False
        if not user.isalnum():
            messages.add_message(request,messages.INFO,'Username must contain one alphabet and one numaric value')
            error = True
        if re.search("'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'", email):
            messages.add_message(request,messages.ERROR,'Email is not in a correct format')
            error = True
        if  password.isalnum():
            messages.add_message(request,messages.INFO,'Password must contain one alphabet and one numaric value')
            error = True
        if password != conform_pass:
            messages.add_message(request,messages.ERROR,'Conform passsword not match')
            error = True
        if error:
            return redirect('SiginUp')
        try:
            User.objects.create_user(user,email,password)    
        except IntegrityError :
            messages.add_message(request,messages.ERROR,'User Already Exists')

    return render(request,'account/register.html')
def Contact_Us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        import re 
        error = False
        email_f = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(email_f,email):
            messages.add_message(request,messages.ERROR,'Email is not valid')
            error = True
        if len(comment) < 10:
            messages.add_message(request,messages.ERROR,'Message is to short')
            error = True
        if len(name) < 3:
            messages.add_message(request,messages.ERROR,'Name is not correct')
            error = True
        if error:
            return render(request,'account/contact.html')
        contact = ContactUs(name=name,email=email,comment=comment)
        contact.save()
        # send_mail(
        # 'Testing',
        # 'Hi iam here Farhan .',
        # 'waqasdevolper@gmail.com',
        # [email],
        # fail_silently=False,
        # )
        plaintext = get_template('email/send.html')
        htmly  = get_template('email/send.html')
        d = {'sender_name':name}
        subject, from_email, to = 'Registration', 'waqasdevolper@gmail.com', email
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.add_message(request,messages.INFO,'We will conatct u soon')
    return render(request,'account/contact.html')