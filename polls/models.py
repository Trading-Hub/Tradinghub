from django.db import models
from django.utils import timezone
# Create your models here.

class BlogDetails(models.Model):
    blogTitle=models.CharField(max_length=100)
    blogProfile=models.ImageField(upload_to="profiles")
    blogImage=models.ImageField(upload_to="profiles")
    blogContant=models.TextField()
    blogDate=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.blogTitle
    
class TodaysNews(models.Model):
    headline=models.CharField(max_length=100)
    newsProfile=models.ImageField(upload_to="profiles")
    article=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.headline
    
class ContactUs(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Subject=models.CharField(max_length=100)
    Message=models.TextField()


class Portfolio(models.Model):
    portfolioName=models.CharField(max_length=50)
    PortfolioTitle=models.CharField(max_length=100)
    portfolioDetails=models.TextField()
    portfolioImage=models.ImageField(upload_to="portfolio")