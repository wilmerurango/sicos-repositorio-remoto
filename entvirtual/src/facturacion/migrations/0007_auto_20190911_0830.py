# Generated by Django 2.2.4 on 2019-09-11 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0006_auto_20190911_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpp_arriendo_detalle',
            name='cpp_arriendo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.cpp_arriendo', verbose_name='N° Factura'),
        ),
    ]
