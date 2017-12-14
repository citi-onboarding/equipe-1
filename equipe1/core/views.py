from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
# Create your views here.

def index(request):

	if request.user.is_authenticated:
		logado = 1
		username = request.user.name

	else:
		logado = 0
		username = ''

	# context{
	# 			'usuario': username,
	# 			'logado': logado,
	# 			'entrou': entrou,
	# }	    
		
	# return render(
	# 	request,
	# 	'index.html',
	# 	context 
	# 	)


def signOut(request):
	if(request.method == POST):
		logout(request)
		return render(request, 'index')

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
		entrou = 0

	if request.user.is_authenticated:
		logado = 1
		username = request.user.name
	else:
		logado = 0
		username = ''

	context = {
				'usuario': username,
				'logado': logado,
				'entrou': entrou,
	}	    

	return render(
		request,
		'logincadastro.html', 
		context
		)



def logOut(request):
	logout(request)
	return render(request, 'index')

def perfil(request):



	return render(
		request,
		'.html', 
		context
		)

def lista(request):

	casas_list = Casa.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(casas_list, 10)
	try:
	    casas = paginator.page(page)
	except PageNotAnInteger:
	    casas = paginator.page(1)
	except EmptyPage:
	    casas = paginator.page(paginator.num_pages)

	return render(request, 'casas_lista.html', { 'casas': casas, 'lista': casas_list, })	


	
