from django.urls import path
from .views import signupfunc,loginfunc,listfunc,msgfunc

urlpatterns = [
    path('signup/', signupfunc,name='signup'),
    path('login/', loginfunc,name='login'),
    path('list/', listfunc, name='list'),
    path('', msgfunc, name='msg')
    
    
]
