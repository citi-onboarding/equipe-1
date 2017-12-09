from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
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
		if (request.POST['action2'] == 'Register'):
			register = RegisterForm(request.POST)
			if register.is_valid():
				register.save()
				username = register.cleaned_data.get('username')
				password = register.cleaned_data.get('password')
				user = authenticate (username = username, password = password)
				if user is not None:
					login(request,user)
				return render(request,'index.html',)
		elif (request.POST['action'] == 'Login'):
			register = RegisterForm(request.POST)
			username = register.cleaned_data.get('username')
			password = register.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request,user)
				return redirect('home')

	else:
		register = RegisterForm()

	context = {
		'form': register
	}

	return render(
		request,
		'formulario.html', 
		context)