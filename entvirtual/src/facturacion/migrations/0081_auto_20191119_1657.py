# Generated by Django 2.2.4 on 2019-11-19 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0080_auto_20191119_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='reten_arrindo',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Retención por Arriendo'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='pension_obligado',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Obligado a Cotizar Pension '),
        ),
    ]
