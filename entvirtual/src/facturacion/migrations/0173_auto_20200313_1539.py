# Generated by Django 2.2.4 on 2020-03-13 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0172_fac_especialista_detalle_parametrizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fac_especialista_detalle',
            name='parametrizado',
            field=models.BooleanField(default=False, null=True, verbose_name='Opcion'),
        ),
    ]
