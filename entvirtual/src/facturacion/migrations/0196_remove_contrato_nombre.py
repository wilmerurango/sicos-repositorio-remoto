# Generated by Django 2.2.4 on 2020-06-09 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0195_auto_20200609_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='nombre',
        ),
    ]