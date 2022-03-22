from turtle import pos
from django.db import models

# Create your models here.
class post(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"

class comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=30)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.content}"

class post_protect(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"

class comment_protect(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=30)
    post = models.ForeignKey(post, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.content}"