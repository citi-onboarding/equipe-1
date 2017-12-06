from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	return render(
		request,
		'index.html',
		)

def signUp(request):
    if(request.method == POST):
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
            	login(request,user)
            	return redirect('home')


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
	return render(
		request,
		'formulario.html',
		)