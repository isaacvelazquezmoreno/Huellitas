from django.db import models

# Create your models here.

class Cita(models.Model):
    C_ESTADO = [('Finalizada', 'Finalizada'), ('Cancelada', 'Cancelada'), ('Confirmada', 'Confirmada'), ('En espera', 'En espera')]
    id_clie = models.ForeignKey('auth.User', related_name='cliente', verbose_name='Cliente', on_delete=models.CASCADE)
    id_vete = models.ForeignKey('auth.User', limit_choices_to={'groups__name': "Veterinario"}, related_name='veterinario', verbose_name='Veterinario', on_delete=models.CASCADE)
    fec_cita = models.DateField(verbose_name='Fecha de la cita')
    est_cita = models.CharField(max_length=20, choices=C_ESTADO, default='En espera', verbose_name='Estado de la cita')