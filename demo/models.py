from unicodedata import name
from django.db import models

# Create your models here.
class menu(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"

class item(models.Model):
    name = models.CharField(max_length=30)
    des = models.CharField(max_length=30)
    menu = models.ForeignKey(menu, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"


class topping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"

class pizza(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(topping)
    def __str__(self):
        return f"{self.name}"

class place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    def __str__(self):
        return f"{self.address}"

class restaurant(models.Model):
    place = models.OneToOneField(
        place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

