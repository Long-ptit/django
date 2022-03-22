from django.db import models

# Create your models here.
from django.db import models


class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='image', default=None)
    desc = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.IntegerField()


class Book(Items):
    author = models.CharField(max_length=50)
    publishingCompany = models.CharField(max_length=50)


class MobilePhone(Items):
    insurance = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50)


class Clothes(Items):
    size = models.CharField(max_length=3)
    material = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)


class Laptop(Items):
    hardware = models.CharField(max_length=50)
    insurance = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50)


class Electronics(Items):
    insurance = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50)


class Shoes(Items):
    size = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=50)
