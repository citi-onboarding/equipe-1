from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
from .models import *

def quemSomos(request):
	return redirect(quemSomosPage)

def index(request):

	if request.user.is_authenticated:
		logado = 1
		username = request.user.name

	else:
		logado = 0
		username = ''

	context = {
				'usuario': username,
				'logado': logado,
	}	    
		
	return render(
		request,
		'home.html',
		context
		)

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
					return redirect(index)
		elif 'logar' in request.POST:
			logar = LoginForm(request.POST)
			if logar.is_valid():
				username = logar.cleaned_data.get('username')
				password = logar.cleaned_data.get('password')
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request,user)
					return redirect(index)

	else:
		register = RegisterForm()
		logar = LoginForm()

	if request.user.is_authenticated:
		logado = 1
		username = request.user.name
	else:
		logado = 0
		username = ''

	context = {
				'usuario': username,
				'logado': logado,
				'register':register
	}	    

	return render(
		request,
		'logincadastro.html', 
		context
		)



def logOut(request):
	logout(request)
	return redirect(index)

def perfil(request):
	if request.user.is_authenticated:
		logado = 1
		username = request.user.name

	else:
		logado = 0
		username = ''

	context = {
				'usuario': username,
				'logado': logado,
	}	    


	return render(
		request,
		'.html', 
		context
		)

def lista(request):
	if request.user.is_authenticated:
		logado = 1
		username = request.user.name

	else:
		logado = 0
		username = ''

	# listadecasas = 
	context = {
				'usuario': username,
				'logado': logado,
				'listadecasas': listadecasas,
	}	    


	return render(
		request,
		'.html', 
		context
		)
