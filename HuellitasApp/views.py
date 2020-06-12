from django.shortcuts import render, HttpResponse
from HuellitasApp import forms
from .models import Producto
# Create your views here.

def index(request):    
    return render(request, "site/home.html")

def products(request):
    products = Producto.objects.all()
    return render(request, "site/products.html", {"products": products})

def login(request):
    login_form = forms.FormLogin()
    return render(request, "usuarios/login.html", {'form': login_form})

def user_register(request):
    return render(request, "site/user-register.html")

def appointment(request):
    return render(request, "site/appointment.html")

#Ejemplo de parámetros, listas y variables con envío de estos al template
def param_num(request, num1, num2):
    nombre = "Isaac Velazquez Moreno"
    lista = ["azul", "rojo", "negro", "blanco", "verde"]
    suma = num1 + num2
    cadena = "La suma de %s + %s = %s" %(num1, num2, suma)
    return render(request, "index.html", {"name":nombre, "colores":lista, "suma":cadena})