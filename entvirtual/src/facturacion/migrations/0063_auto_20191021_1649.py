# Generated by Django 2.2.4 on 2019-10-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0062_reten_383_resta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retencion',
            name='re_base_grav_reten_uvt',
            field=models.FloatField(default=0, null=True, verbose_name='Base Gravable en UVT'),
        ),
    ]
