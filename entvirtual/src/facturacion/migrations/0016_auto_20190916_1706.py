# Generated by Django 2.2.4 on 2019-09-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0015_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpp_arriendo_detalle',
            name='cpp_arriendo',
            field=models.IntegerField(null=True, verbose_name='N° Factura'),
        ),
    ]
