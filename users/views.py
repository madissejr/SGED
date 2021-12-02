from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm

from sged.decorators import naoAutenticado

# Create your views here.

#Metodo para entrar no sistema
@naoAutenticado
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    
    return render(request, 'users/login.html')

#metodo para sair do sistema
def userLogout(request):
    logout(request)
    return redirect('user:entrar')
