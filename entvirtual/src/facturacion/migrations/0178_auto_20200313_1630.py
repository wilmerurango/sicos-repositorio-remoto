# Generated by Django 2.2.4 on 2020-03-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0177_auto_20200313_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fac_especialista_detalle',
            name='parametrizado',
            field=models.BooleanField(default=False, null=True),
        ),
    ]