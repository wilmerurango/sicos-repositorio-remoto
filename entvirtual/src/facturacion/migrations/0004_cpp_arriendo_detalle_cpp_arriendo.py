# Generated by Django 2.2.4 on 2019-09-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_remove_cpp_arriendo_detalle_cpp_arriendo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp_arriendo_detalle',
            name='cpp_arriendo',
            field=models.IntegerField(max_length=100, null=True, verbose_name='N° Factura'),
        ),
    ]
