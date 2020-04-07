# Generated by Django 2.2.4 on 2019-10-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0047_auto_20191018_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='glosa',
        ),
        migrations.AddField(
            model_name='fac_especialista',
            name='glosa',
            field=models.FloatField(default=0, null=True, verbose_name='Glosa del mes'),
        ),
    ]