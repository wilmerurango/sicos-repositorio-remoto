# Generated by Django 2.2.4 on 2019-12-30 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0088_auto_20191230_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribucion',
            name='centro_costo',
        ),
    ]