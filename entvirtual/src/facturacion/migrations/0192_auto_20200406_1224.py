# Generated by Django 2.2.4 on 2020-04-06 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0191_remove_cpp_proveedor_detalle_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpp_proveedor',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.producto', verbose_name='Producto'),
        ),
    ]
