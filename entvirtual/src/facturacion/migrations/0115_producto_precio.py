# Generated by Django 2.2.4 on 2020-01-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0114_auto_20200107_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=0, null=True, verbose_name='Precio del Producto'),
        ),
    ]