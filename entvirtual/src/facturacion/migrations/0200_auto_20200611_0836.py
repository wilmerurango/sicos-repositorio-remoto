# Generated by Django 2.2.4 on 2020-06-11 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0199_auto_20200610_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialista',
            name='fechafact_esp',
            field=models.DateField(default=datetime.date(2020, 6, 11), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='uvt',
            name='rent_ext_lab',
            field=models.FloatField(default=0, null=True, verbose_name='Renta Extensa Laboral en %'),
        ),
    ]
