# Generated by Django 2.2.4 on 2020-01-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0091_distribucion_centro_costo'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='distri_fija',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='¿Distribución Porcentual?'),
        ),
    ]
