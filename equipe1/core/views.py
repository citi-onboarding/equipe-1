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

def signIn(request):
	if(request.method == POST):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('home')


def signOut(request):
	if(request.method == POST):
		logout(request)
		return redirect('home')

def logIn(request):
	if(request.method == 'POST'):
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate (username = username, password = password)
			if user is not None:
				login(request,user)
			return render(request,'index.html',)
	else:
		form = RegisterForm()
	return render(
		request,
		'formulario.html',
		{'form' : form}
		)