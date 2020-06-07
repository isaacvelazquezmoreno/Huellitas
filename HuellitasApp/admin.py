from django.contrib import admin
from HuellitasApp import models

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ("mod_producto", "id_tipo", "id_mar", "pre_uni", "stock_pro", "updated_at")
    search_fields = ("id_mar", "id_tipo")
    list_filter = ("updated_at",)

class CitasAdmin(admin.ModelAdmin):
    list_display = ("id_clie", "id_vete", "fec_cita", "est_cita")
    search_fields = ("est_cita",)
    list_filter = ("fec_cita",)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("id_usu", "id_pro", "can_ped")

class OrdenAdmin(admin.ModelAdmin):
    list_display = ("total_ord", "pago_ord", "envio_ord", "fec_ord")

class OrdenPedidoAdmin(admin.ModelAdmin):
    list_display = ("id_ord", "id_ped")

admin.site.register(models.Cita, CitasAdmin)
admin.site.register(models.Producto, ProductosAdmin)
admin.site.register(models.Pedido, PedidosAdmin)
admin.site.register(models.Orden, OrdenAdmin)
admin.site.register(models.OrdenPedido, OrdenPedidoAdmin)