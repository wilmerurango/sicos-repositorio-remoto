# Generated by Django 2.2.4 on 2019-09-20 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0022_auto_20190919_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='aport_volun_pension',
            field=models.FloatField(default=0, null=True, verbose_name='Aportes Voluntarios a Pension'),
        ),
        migrations.AddField(
            model_name='uvt',
            name='rent_ext_lab',
            field=models.FloatField(default=0, null=True, verbose_name='Renta Extensa Laboral'),
        ),
        migrations.AddField(
            model_name='uvt',
            name='tope_deduc_re',
            field=models.FloatField(default=0, null=True, verbose_name='Tope Renta Extensa en %'),
        ),
        migrations.AlterField(
            model_name='fac_especialista_detalle',
            name='honorario',
            field=models.FloatField(default=0, null=True, verbose_name='Honorario'),
        ),
    ]
