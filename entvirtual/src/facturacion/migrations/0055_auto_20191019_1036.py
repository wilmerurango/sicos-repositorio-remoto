# Generated by Django 2.2.4 on 2019-10-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0054_auto_20191019_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retencion',
            name='incr_aport_vol_pension',
            field=models.FloatField(default=0, null=True, verbose_name='Aportes Voluntarios a Pension'),
        ),
    ]