# Generated by Django 2.2.4 on 2020-02-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0137_distri_serv_public_boolean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distri_serv_public',
            name='boolean',
            field=models.BooleanField(default=True),
        ),
    ]
