# Generated by Django 2.2.4 on 2020-02-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0148_cpp_serv_public_reten'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descrip',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
    ]
