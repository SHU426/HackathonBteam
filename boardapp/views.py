from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import authenticate, login
from .models import Board

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

def listfunc(request):
    return render(request,'list.html',{})

def index(request):
    latest_board_list = Board.objects.order_by('create_at')
    context = {
        'latest_board_list':latest_board_list,
    }
    return render(request,'boardapp/index.html',context)

def detail(request,board_id):
    board = get_object_or_404(Board,pk=board_id)
    return render(request,'boardapp/msg.html',{'board':board})