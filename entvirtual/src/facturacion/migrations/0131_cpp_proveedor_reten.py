# Generated by Django 2.2.4 on 2020-01-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0130_auto_20200113_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp_proveedor',
            name='reten',
            field=models.FloatField(default=2.5, null=True, verbose_name='Retención'),
        ),
    ]
