# Generated by Django 2.2.4 on 2020-04-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0182_auto_20200402_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp_proveedor_detalle',
            name='option',
            field=models.BooleanField(default=True, null=True, verbose_name='¿Parametrizado?'),
        ),
    ]
