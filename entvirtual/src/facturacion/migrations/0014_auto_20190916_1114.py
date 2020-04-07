# Generated by Django 2.2.4 on 2019-09-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0013_inductor_arri_cuenta_especific'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp_arriendo_detalle',
            name='cuenta_especific',
            field=models.CharField(max_length=100, null=True, verbose_name='Cuenta Especifica'),
        ),
        migrations.AlterField(
            model_name='cpp_arriendo_detalle',
            name='num_cuenta',
            field=models.CharField(max_length=100, null=True, verbose_name='Cuenta C. Costo'),
        ),
    ]
