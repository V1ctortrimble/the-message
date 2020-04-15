from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=',request.user,'Entrou -=-=-=-=-=-=-=-=-=-=-=-=-=' )
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Usuário ou Senha Ivalidos, Tente Novamente')
    return redirect('/login/')


@login_required(login_url='/login')
def home (request):
    return render(request,'home.html')

def logout_user(request):
    print ('-=-=-=-=-=-=-=-=-=-=-=-=-=',request.user,'Saiu -=-=-=-=-=-=-=-=-=-=-=-=-=')
    logout(request)
    return redirect ('/login/')

def perfil_user(request):
    user = User.objects.filter(ativo=True, user=request.user)
    return render(request, 'perfil.html', {'user_model': user})

def registrar_user(request):
    return render(request, 'registrar.html')

def recuper_senha_user(request):
    return render(request, 'recuperarsenha.html')