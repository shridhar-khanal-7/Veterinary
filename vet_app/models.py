from django.db import models

# Create your models here.


class Contact(models.Model):
        name=models.CharField(max_length=50,blank=False,default='shree')
        email=models.EmailField(max_length=20,blank=False,default='your@example.com')
        phone=models.CharField(max_length=10, blank=False,default='9858585959')
        desc=models.TextField(default='Hello, world')
        date=models.DateField(default='2001-01-01')        