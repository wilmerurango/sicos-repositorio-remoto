# Generated by Django 2.2.4 on 2019-10-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0058_auto_20191021_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='fac_especialista',
            name='rent_exten_lab',
            field=models.FloatField(default=25, null=True, verbose_name='Renta Extensa Laboral'),
        ),
    ]
