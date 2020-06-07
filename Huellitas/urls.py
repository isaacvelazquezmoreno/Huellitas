"""Huellitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HuellitasApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('productos/', views.products),
    path('login/', views.login),
    path('registro/', views.user_register),
    path('citas/', views.dates),
    path('agendar/', views.appointment),
    # Ejemplo URL con dos parámetros numéricos
    path('suma/<int:num1>/<int:num2>/', views.param_num),
]
