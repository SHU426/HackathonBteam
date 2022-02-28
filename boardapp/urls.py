from django.urls import path
from .views import signupfunc,loginfunc,listfunc,index,detail

urlpatterns = [
    path('signup/', signupfunc,name='signup'),
    path('login/', loginfunc,name='login'),
    path('list/', listfunc, name='list'),
    # ex:/boardapp/
    path('', index , name='board'),
    # ex:/boardapp/1/
    path('<int:board_id>/',detail,name='detail'),
    
    
]
