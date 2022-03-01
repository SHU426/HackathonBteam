from django.urls import path
from .views import logoutfunc, signupfunc,loginfunc,sredfunc,boardfunc,BoardCreate,BoardDelete

urlpatterns = [
    path('', signupfunc,name='signup'),
    path('login/', loginfunc,name='login'),
    path('sred/', sredfunc, name='sred'),
    path('board/', boardfunc, name='board'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('delete/<int:pk>', BoardDelete.as_view(), name='delete'),
    path('logout/', logoutfunc,name='logout')
]
