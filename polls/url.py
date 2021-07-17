from django.contrib import admin
from django.urls import path
from polls import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path("home",views.index,name="index"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("portfolio",views.portfolio,name="portfolio"),
    path("portfolio-details",views.portfolio_details,name="portfolio_details"),
    path("blog",views.blog,name="blog"),
    path("blog-details",views.blog_details,name="blog_details"),
    path("contact",views.contact,name="contact"),
    path("dataSend",views.dataSend,name="dataSend"),
    path("news-single",views.newsSingle,name="news-single"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
