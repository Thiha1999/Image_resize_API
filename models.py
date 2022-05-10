
from msilib.schema import Class
from tkinter.ttk import Style
from turtle import width
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField

class Fish(models.Model):

    id = models.AutoField(primary_key=True)
    fishname = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    weight = models.FloatField()
    length = models.FloatField()
    latitude = models.CharField(max_length=200 ,blank=True)
    longitude = models.CharField(max_length=200 ,blank=True)
    image = ResizedImageField(size=[140, 140],upload_to='upload/image',blank=True ,max_length=200)
    uploaded = models.DateTimeField(default=timezone.now)




