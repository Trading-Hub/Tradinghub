from datetime import datetime, time
from .models import BlogDetails,TodaysNews,ContactUs
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.http import HttpResponse, request
from django.contrib import messages
from django.conf import settings as conf_settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,"index.html",{})

def about(request):
    return render(request,"aboutus.html",{})

def services(request):
    return render(request,"service.html",{})

def terms(request):
    return render(request,"tos.html",{})

def privacy(request):
    return render(request,"privicy.html",{})

def blog(request):
    blog=BlogDetails.objects.all()
    template_paginator = Paginator(blog, 4)
    page_num = request.GET.get('page')
    page = template_paginator.get_page(page_num)

    today = datetime.now().date()
    news=TodaysNews.objects.filter(date=today)
    return render(request,"blog.html",{"blog":page,"news":news})

def blog_details(request):
    blogId=request.GET["id"]
    blog=BlogDetails.objects.get(id=blogId)
    today = datetime.now().date()
    news=TodaysNews.objects.filter(date=today)
    return render(request,"blog-single.html",{"blog":blog,"news":news})

def contact(request):
    return render(request,"contact.html",{})

def newsSingle(request):
    newsId=request.GET["id"]
    news=TodaysNews.objects.get(id=newsId)
    return render(request,"news-single.html",{"news":news})

def dataSend(request):
    if request.POST:
        name=request.POST["name"]
        email=request.POST["email"]
        sub=request.POST["subject"]
        mes=request.POST["message"]
        
        data=ContactUs(Name=name, Email=email, Subject=sub, Message=mes)
        data.save()
        messages.info(request,'Your message has been sent. Thank you!')

        subject = 'Thanks for contacting us'
        message = f'Thank you for contacting us, our team will soon respond you. Please drop your message on whatsapp for inquries. This is computer generated e-mail please do not reply.'
        email_from = conf_settings.EMAIL_HOST_USER 
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        

        return redirect('/contact')
    else:
        return redirect('/contact')
