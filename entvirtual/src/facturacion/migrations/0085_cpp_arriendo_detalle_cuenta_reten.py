# Generated by Django 2.2.4 on 2019-12-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0084_auto_20191227_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp_arriendo_detalle',
            name='cuenta_reten',
            field=models.CharField(max_length=60, null=True, verbose_name='Cuenta Retenedora'),
        ),
    ]