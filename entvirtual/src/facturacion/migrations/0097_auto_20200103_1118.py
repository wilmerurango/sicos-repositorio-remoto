# Generated by Django 2.2.4 on 2020-01-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0096_auto_20200103_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpp_proveedor_detalle',
            name='valor',
            field=models.FloatField(default=0, null=True, verbose_name='Valor'),
        ),
    ]