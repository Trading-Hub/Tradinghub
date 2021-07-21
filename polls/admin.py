from django.contrib import admin
from .models import BlogDetails,TodaysNews,ContactUs

class blog_display(admin.ModelAdmin):
    list_display = ['blogTitle','blogProfile','blogImage','blogContant','blogDate']

class news_display(admin.ModelAdmin):
    list_display = ['headline','newsProfile','article','date']

class contact_display(admin.ModelAdmin):
    list_display = ['Name','Email','Subject','Message']
    


# Register your models here.
admin.site.register(BlogDetails , blog_display)
admin.site.register(TodaysNews , news_display)
admin.site.register(ContactUs,contact_display)