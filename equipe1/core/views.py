from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
# Create your views here.

def index(request):
	return render(
		request,
		'index.html',
		)

def signOut(request):
	if(request.method == POST):
		logout(request)
		return redirect('home')
def logIn(request):
	
	if(request.method == 'POST'):
		if 'cadastro' in request.POST:
			register = RegisterForm(request.POST)
			if register.is_valid():
				register.save()
				username = register.cleaned_data.get('username')
				password = register.cleaned_data.get('password')
				user = authenticate (username = username, password = password)
				if user is not None:
					login(request,user)
					return render(request,'index.html',)
		elif 'logar' in request.POST:
			entrou = 1;
			logar = LoginForm(request.POST)
			if logar.is_valid():
				username = logar.cleaned_data.get('username')
				password = logar.cleaned_data.get('password')
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request,user)
					return render(request,'index.html',)

	else:
	    register = RegisterForm()
	    logar = LoginForm()

	if request.user.is_authenticated:
		logado = 1
		username = request.user.name
	else:
		logado = 0
		username = 'gfsca'

	context = {
				'usuario': username,
				'logado': logado,
				'entrou': entrou,
	}	    

	return render(
		request,
		'formulario.html', 
		context
		)


def logOut(request):
	logout(request)
	return render(request, 'index.html')

