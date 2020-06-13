from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
    C_TIPO = [('Alimento', 'Alimento'),('Accesorio', 'Accesorio')]
    C_COLOR = [('Negro', 'Negro'),('Rojo', 'Rojo'),('Azul', 'Azul'),('Amarillo', 'Amarillo'),('Verde', 'Verde')]
    C_MATERIAL = [('Plástico', 'Plástico'),('Orgánico', 'Orgánico'),('Sintético', 'Sintético')]
    C_ORIGEN = [('Nacional', 'Nacional'),('Importado', 'Importado'),('Chino', 'Chino')]
    C_MARCA = [('Pedigree', 'Pedigree'),('Whiskas','Whiskas'),('Bayer','Bayer'),('Pets happy','Pets happy')]
    mod_producto = models.CharField(max_length=30, verbose_name='Modelo')
    id_tipo = models.CharField(max_length=50, choices=C_TIPO, verbose_name='Tipo de producto')
    id_color = models.CharField(max_length=50, choices=C_COLOR, verbose_name='Color')
    id_mat = models.CharField(max_length=50, choices=C_MATERIAL, verbose_name='Tipo de material')
    id_ori = models.CharField(max_length=20, choices=C_ORIGEN, verbose_name='Origen')
    id_mar = models.CharField(max_length=50, choices=C_MARCA, verbose_name='Marca')
    descri = models.CharField(max_length=300, default='Aqui hay una descripcion' ,verbose_name='Descripcion')
    pre_uni = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio unitario')
    stock_pro = models.IntegerField(verbose_name='Productos en existencia')
    img_pro = models.CharField(max_length=200, verbose_name='URL de imagen de producto', blank=True, default='/statics/images-site/pets/02.jpg')
    created_at = models.DateField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateField(auto_now=True, verbose_name='Actualizado')

    def __str__(self):
        return "Producto: %s - Tipo: %s - Marca: %s" %(self.mod_producto, self.id_tipo, self.id_mar)

class Pedido(models.Model):
    id_usu = models.ForeignKey('auth.User', verbose_name='Cliente', on_delete=models.CASCADE)
    id_pro = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.CASCADE)
    can_ped = models.IntegerField(verbose_name='Cantidad de productos')

    def __str__(self):
        return "Pedido de %s, producto: %s" %(self.id_usu, self.id_pro)

class Orden(models.Model):
    total_ord = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio total')
    pago_ord = models.BooleanField(default=False, verbose_name='Se pagó el pedido')
    envio_ord = models.BooleanField(default=False, verbose_name='Se realizó el envío')
    fec_ord = models.DateField(auto_now_add=True, verbose_name='Fecha de orden')
    
    def __str__(self):
        return "Orden %s - total: %s - pagado: %s - enviado: %s" %(self.fec_ord ,self.total_ord, self.pago_ord, self.envio_ord)

class OrdenPedido(models.Model):
    id_ord = models.ForeignKey(Orden, verbose_name='Orden', on_delete=models.CASCADE)
    id_ped = models.ForeignKey(Pedido, verbose_name='Pedido', on_delete=models.CASCADE)
