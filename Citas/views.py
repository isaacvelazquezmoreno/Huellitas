from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Cita 
from .forms import RegisterAppointment
# Create your views here.


def appointment(request):
    # User.objects.filter(groups__name='Staff')
    # appointment = Cita.objects.filter(groups__name='Veterinario')
    return render(request, "citas/appointment.html", ) 
    

def add_appointment(request):
    if request.method == 'POST':
        form = RegisterAppointment(request.POST)
        # form_appotiment = Cita('id_clie'=request.user, 'id_vete'=)
        if form.is_valid():
            vet = form.cleaned_data['vets']
            day = form.cleaned_data['day']
            c = Cita(id_clie=request.user, id_vete=vet, fec_cita=day)
            c.save()
            return redirect("/citas")
    else:
        # vets = User.objects.filter(groups__name='Veterinario')
        form = RegisterAppointment()
    return render( request, "citas/appointment-register.html", {"form": form} )