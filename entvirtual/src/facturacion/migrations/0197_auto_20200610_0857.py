# Generated by Django 2.2.4 on 2020-06-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0196_remove_contrato_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialista',
            name='dir_esp',
            field=models.CharField(blank=True, max_length=100, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='mail_esp',
            field=models.EmailField(blank=True, max_length=60, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='tel_esp',
            field=models.CharField(blank=True, max_length=12, verbose_name='Telefono'),
        ),
    ]