# Generated by Django 2.2.4 on 2020-03-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0179_auto_20200313_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fac_especialista_detalle',
            name='parametrizado',
            field=models.BooleanField(default=True, null=True, verbose_name='Opcion'),
        ),
    ]