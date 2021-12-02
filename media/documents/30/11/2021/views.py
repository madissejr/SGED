from django.conf import settings
from django.shortcuts import redirect, render
from .decorator import naoAutenticado
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
        
        
   