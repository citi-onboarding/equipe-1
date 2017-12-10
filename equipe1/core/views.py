from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect
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
				# username = register.cleaned_data.get('username')
				# password = register.cleaned_data.get('password')
				# user = authenticate (username = username, password = password)
				# if user is not None:
				# 	login(request,user)
				# 	return render(request,'index.html',)
		elif 'logar' in request.POST:
			logar = LoginForm(request.POST)
			if logar.is_valid():
				username = logar.cleaned_data.get('username')
				password = logar.cleaned_data.get('password')
				user = authenticate(request, username=username, password=password)
				if user is not None:
					login(request,user)
					print("LOGUEI")
					return render(request,'index.html',)

	else:
	    register = RegisterForm()
	    logar = LoginForm()


	return render(
		request,
		'formulario.html', 
		
		)


def logOut(request):
	logout(request)
	return render(request, 'index.html')

