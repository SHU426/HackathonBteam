from django.urls import path
from .views import signupfunc,loginfunc,sredfunc,boardfunc

urlpatterns = [
    path('signup/', signupfunc,name='signup'),
    path('login/', loginfunc,name='login'),
    path('sred/', sredfunc, name='sred'),
    path('board/', boardfunc, name='board')
]
