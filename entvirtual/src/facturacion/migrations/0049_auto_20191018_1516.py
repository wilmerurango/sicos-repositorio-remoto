# Generated by Django 2.2.4 on 2019-10-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0048_auto_20191018_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retencion',
            name='fac_especialista',
            field=models.IntegerField(default=0, null=True, verbose_name='Factura'),
        ),
    ]
