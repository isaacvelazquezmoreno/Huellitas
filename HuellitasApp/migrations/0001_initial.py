# Generated by Django 3.0.6 on 2020-06-07 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_ord', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Precio total')),
                ('pago_ord', models.BooleanField(default=False, verbose_name='Se pagó el pedido')),
                ('envio_ord', models.BooleanField(default=False, verbose_name='Se realizó el envío')),
                ('fec_ord', models.DateField(auto_now_add=True, verbose_name='Fecha de orden')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod_producto', models.CharField(max_length=30, verbose_name='Modelo')),
                ('id_tipo', models.CharField(choices=[('Alimento', 'Alimento'), ('Accesorio', 'Accesorio')], max_length=50, verbose_name='Tipo de producto')),
                ('id_color', models.CharField(choices=[('Negro', 'Negro'), ('Rojo', 'Rojo'), ('Azul', 'Azul'), ('Amarillo', 'Amarillo'), ('Verde', 'Verde')], max_length=50, verbose_name='Color')),
                ('id_mat', models.CharField(choices=[('Plástico', 'Plástico'), ('Orgánico', 'Orgánico'), ('Sintético', 'Sintético')], max_length=50, verbose_name='Tipo de material')),
                ('id_ori', models.CharField(choices=[('Nacional', 'Nacional'), ('Importado', 'Importado'), ('Chino', 'Chino')], max_length=20, verbose_name='Origen')),
                ('id_mar', models.CharField(choices=[('Pedigree', 'Pedigree'), ('Whiskas', 'Whiskas'), ('Bayer', 'Bayer'), ('Pets happy', 'Pets happy')], max_length=50, verbose_name='Marca')),
                ('pre_uni', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Precio unitario')),
                ('stock_pro', models.IntegerField(verbose_name='Productos en existencia')),
                ('img_pro', models.CharField(blank=True, default='/statics/images-site/pets/02.jpg', max_length=200, verbose_name='URL de imagen de producto')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Actualizado')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_ped', models.IntegerField(verbose_name='Cantidad de productos')),
                ('id_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HuellitasApp.Producto', verbose_name='Producto')),
                ('id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HuellitasApp.Orden', verbose_name='Orden')),
                ('id_ped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HuellitasApp.Pedido', verbose_name='Pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fec_cita', models.DateField(verbose_name='Fecha de la cita')),
                ('est_cita', models.CharField(choices=[('Finalizada', 'Finalizada'), ('Cancelada', 'Cancelada'), ('Confirmada', 'Confirmada'), ('En espera', 'En espera')], default='En espera', max_length=20, verbose_name='Estado de la cita')),
                ('id_clie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
                ('id_vete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veterinario', to=settings.AUTH_USER_MODEL, verbose_name='Veterinario')),
            ],
        ),
    ]