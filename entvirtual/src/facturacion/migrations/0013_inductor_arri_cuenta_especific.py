# Generated by Django 2.2.4 on 2019-09-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0012_auto_20190911_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='inductor_arri',
            name='cuenta_especific',
            field=models.CharField(max_length=20, null=True, verbose_name='Cuenta Espesifica'),
        ),
    ]