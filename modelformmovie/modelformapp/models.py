from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField()
    cast=models.CharField(max_length=38)
    release=models.CharField(max_length=10)
    gener=models.CharField(max_length=35)

