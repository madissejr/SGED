from django.contrib import auth
from django.urls import path

from django.contrib.auth import views
from users.forms import UserChangePassword

from users.views import userLogin, userLogout


app_name = 'user'
urlpatterns = [
    path('entrar/', userLogin, name='entrar'),
    path('sair/', userLogout, name='sair'),
]
