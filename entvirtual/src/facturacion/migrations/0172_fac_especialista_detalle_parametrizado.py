# Generated by Django 2.2.4 on 2020-03-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0171_remove_uvt_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='parametrizado',
            field=models.BooleanField(null=True),
        ),
    ]
