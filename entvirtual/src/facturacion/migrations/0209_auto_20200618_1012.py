# Generated by Django 2.2.4 on 2020-06-18 15:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0208_auto_20200618_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='cargo_esp',
            field=models.CharField(blank=True, max_length=70, verbose_name='Cargo del Especialista'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 6, 18, 15, 12, 6, 378384, tzinfo=utc), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor',
            field=models.FloatField(default=0, verbose_name='Monto Devengado al mes'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='fechafact_esp',
            field=models.DateField(default=datetime.datetime(2020, 6, 18, 15, 12, 6, 378384, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
    ]
