# Generated by Django 2.2.4 on 2020-06-10 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0198_especialista_especialidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialista',
            name='fechafact_esp',
            field=models.DateField(default=datetime.date(2020, 6, 10), verbose_name='Fecha de Registro'),
        ),
    ]
