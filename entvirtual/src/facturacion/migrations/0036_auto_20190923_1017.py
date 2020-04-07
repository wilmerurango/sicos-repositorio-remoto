# Generated by Django 2.2.4 on 2019-09-23 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0035_auto_20190923_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='especialista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.especialista', verbose_name='Nombre del Especialista'),
        ),
        migrations.AlterField(
            model_name='especialista_cpp_aux',
            name='contrato',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.contrato', verbose_name='Identificación Especialista'),
        ),
    ]
