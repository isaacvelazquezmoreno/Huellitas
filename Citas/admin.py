from django.contrib import admin
from Citas import models

# Register your models here.
class CitasAdmin(admin.ModelAdmin):
    list_display = ("id_clie", "id_vete", "fec_cita", "est_cita")
    search_fields = ("est_cita",)
    list_filter = ("fec_cita",)
    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super().save_model(request, obj, form, change)

admin.site.register(models.Cita, CitasAdmin)