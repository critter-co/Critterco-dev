from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models

class Biz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    phone = PhoneNumberField()
    gallery = models.ImageField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    hours = models.CharField(max_length=255, blank=True, null=True)
    location = models.PointField(blank=True, null=True)
