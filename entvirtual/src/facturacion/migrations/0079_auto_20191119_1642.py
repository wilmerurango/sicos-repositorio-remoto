# Generated by Django 2.2.4 on 2019-11-19 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0078_auto_20191119_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta_reten',
            name='contrato',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.contrato', verbose_name='Base Retención-Especialista'),
        ),
    ]