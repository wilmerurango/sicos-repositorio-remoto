# Generated by Django 2.2.4 on 2020-06-18 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0206_auto_20200612_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialista',
            name='apellidos_esp',
            field=models.CharField(blank=True, max_length=70, verbose_name='Apellidos del Especialista'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='fechafact_esp',
            field=models.DateField(default=datetime.datetime(2020, 6, 18, 13, 42, 1, 9758, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
    ]