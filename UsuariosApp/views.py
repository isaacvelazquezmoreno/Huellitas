from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group



def home_view(request):
	return render(request, 'index.html')

# Create your views here.

def signup_view(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		usr = form.save()
		g = Group.objects.get(name='Cliente')
		usr.groups.add(g)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('home')
	return render(request, 'usuarios/registro.html', {'form': form})
