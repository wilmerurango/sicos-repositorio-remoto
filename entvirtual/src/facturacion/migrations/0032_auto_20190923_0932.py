# Generated by Django 2.2.4 on 2019-09-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0031_auto_20190923_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='pct_iss',
            field=models.FloatField(default=25, null=True, verbose_name='Porcentaje ISS Adicional (%)'),
        ),
    ]
