# Generated by Django 2.2.4 on 2020-02-22 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0150_tipo_serv'),
    ]

    operations = [
        migrations.AddField(
            model_name='serv_public',
            name='tipo_serv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.tipo_serv', verbose_name='Tipo de Servicio'),
        ),
    ]
