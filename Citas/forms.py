from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Cita

class DateInput(forms.DateTimeInput):
    input_type = 'date' 

class RegisterAppointment(forms.Form):
    vets = forms.ModelChoiceField( User.objects.filter(groups__name='Veterinario'), label='vets',initial=0)
    day = forms.DateField(label='day' ,widget=DateInput)

# class RegisterAppointment(forms.ModelForm):
#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super(RegisterAppointment, self).__init__(*args, **kwargs)

#     def save(self, commit=True):
#         m = super(CallResultTypeForm, self).save(commit=False)
#         # do custom stuff
#         print(m.id_clie)
#         if commit:
#             m.save()
#         return m 
    
#     # veterinario = forms.ModelChoiceField(User.objects.filter(groups__name='Veterinario'), initial=0)
#     # dia = forms.DateTimeField( widget=)
    
#     class Meta:
#        today = date.today()
#        model = Cita
#        fields = '__all__'
#        exclude = ['id_clie', 'est_cita']
#        widgets = {'fec_cita': DateInput(attrs={'min':today}),}   