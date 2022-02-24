from ast import Delete
from venv import create
from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=255,verbose_name='名前')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='作成日')
    delete_flg = models.SmallIntegerField(verbose_name='削除フラグ',default=0)

def __str__(self):
    return self.username

# class Board(models.Model):
#     board_id = models.IntegerField()

