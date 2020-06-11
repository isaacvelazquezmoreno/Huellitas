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
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from HuellitasApp import views
from UsuariosApp import views as vu
from Citas import views as vc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('productos/', views.products),
    path('registro/', views.user_register),
    path('agendar/', views.appointment),
    path('registrar/', vu.signup_view),
    path('login/', vu.login_request),
    path('logout/', vu.logout_request, name="logout"),
    path('home/', vu.home_user, name="home"),
    path('citas/', vc.appointment),
    path('citas/agendar/', vc.add_appointment),
    # Ejemplo URL con dos parámetros numéricos
    path('suma/<int:num1>/<int:num2>/', views.param_num),
    
]
