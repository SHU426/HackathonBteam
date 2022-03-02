from ast import Delete
from dataclasses import field
from tempfile import template
from winreg import DeleteValue
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import SredModel
from django.views.generic import CreateView,DeleteView
# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            login(request, user)
            return redirect('sred')
        except IntegrityError:
            return render(request,'signup.html',{'error':' このユーザーはすでに登録されています。'})
    return render(request,'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sred')
        else:
            return render(request,'login.html',{'context':'ユーザーネーム又はパスワードを正しく入力してください'})
    return render(request,'login.html')

@login_required
def sredfunc(request):
    object_list = SredModel.objects.all()
    return render(request,'sred.html',{'object_list':object_list})


def boardfunc(request):
    return render(request,'board.html',{})


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = SredModel
    fields = ('title','memo','author')
    success_url = reverse_lazy('sred')

class BoardDelete(DeleteView):
    template_name = 'delete.html'
    model = SredModel
    fields = ('title','memo','author')
    success_url = reverse_lazy('sred')

def logoutfunc(request):
    logout(request)
    return redirect('login')

    