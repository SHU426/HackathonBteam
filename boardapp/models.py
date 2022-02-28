from ast import Delete
from venv import create
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255,verbose_name='名前')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='作成日')
    delete_flg = models.SmallIntegerField(verbose_name='削除フラグ',default=0)

def __str__(self):
    return self.username

class Board(models.Model):
    board_title = models.CharField(max_length=255,verbose_name='タイトル')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='作成日')
    delete_flg = models.SmallIntegerField(verbose_name='削除フラグ',default=0)
    def __str__(self):
        return self.board_title

class Msg_detail(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    msg_detail = models.CharField(max_length=255,verbose_name='タイトル')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='作成日')
    delete_flg = models.SmallIntegerField(verbose_name='削除フラグ',default=0)
    def __str__(self):
        return self.msg_detail

