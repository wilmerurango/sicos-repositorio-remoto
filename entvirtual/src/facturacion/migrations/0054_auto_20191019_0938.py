# Generated by Django 2.2.4 on 2019-10-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0053_auto_20191019_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retencion',
            name='name_especialista',
            field=models.CharField(max_length=30, null=True, verbose_name='Nombre Especialista'),
        ),
    ]