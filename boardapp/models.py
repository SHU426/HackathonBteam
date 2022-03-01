from turtle import title
from django.db import models

# Create your models here.
class SredModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    # (null=True,blank=True)は空のデータベースが使える

    def __str__(self):
        return self.title
        