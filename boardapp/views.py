from dataclasses import field
from tempfile import template
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from .models import SredModel
from django.views.generic import CreateView
# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request,'signup.html',{'some':'Hello World'})
        except IntegrityError:
             return render(request,'signup.html',{'error':' このユーザーはすでに登録されています。'})
    return render(request,'signup.html',{'some':'Hello World'})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'login.html',{'context':'logged in'})
        else:
            return render(request,'login.html',{'context':'not logged in'})
    return render(request,'login.html',{'context':'get method'})

def sredfunc(request):
    object_list = SredModel.objects.all()
    return render(request,'sred.html',{'object_list':object_list})


def boardfunc(request):
    return render(request,'board.html',{})


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = SredModel
    fields = ('title','memo')
    success_url = reverse_lazy('sred')
    