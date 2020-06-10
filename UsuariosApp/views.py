from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages

# Create your views here.
def home_view(request):
	return render(request, 'index.html')

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
		return render(request, 'usuarios/home.html')
	return render(request, 'usuarios/registro.html', {'form': form})

def home_user(request):
	return render(request, 'usuarios/home.html')

def logout_request(request):
	logout(request)	
	return  render(request, 'site/home.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return render(request, 'usuarios/home.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request, template_name = "usuarios/login.html", context={"form":form})