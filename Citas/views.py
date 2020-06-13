from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.http import JsonResponse
import json

from .models import Cita 
from .forms import RegisterAppointment
# Create your views here.


def appointment(request):
    appointments = Cita.objects.filter(id_clie=request.user)
    return render(request, "citas/appointment.html", {"appointments": appointments}) 
    

def add_appointment(request):
    if request.method == 'POST':
        form = RegisterAppointment(request.POST)
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

def update_appointment_client(request):
    data = json.loads(request.body)
    # appointment = Cita(id=, )
    appointment = Cita.objects.get(pk=data['appoitmentId'])
    appointment.est_cita=data['action']
    appointment.save()
    return JsonResponse('El estado de la cita ha sido actualizada', safe=False)