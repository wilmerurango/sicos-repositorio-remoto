# Generated by Django 2.2.4 on 2020-03-30 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0041_auto_20200330_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salario',
            name='rubro',
        ),
    ]
