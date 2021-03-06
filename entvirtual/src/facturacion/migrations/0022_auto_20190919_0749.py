# Generated by Django 2.2.4 on 2019-09-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0021_auto_20190917_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='deduc_depen_cargo',
            field=models.FloatField(default=0, null=True, verbose_name='Dependinte de Cargo'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='deduc_int_prest_vivienda',
            field=models.FloatField(default=0, null=True, verbose_name='Intereses Prestamo Viviendas'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='deduc_plan_comp_salud',
            field=models.FloatField(default=0, null=True, verbose_name='Plan Complementario Salud'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='honorario',
            field=models.FloatField(default=0, null=True, verbose_name='Honoraio'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='incr_aport_arl',
            field=models.FloatField(default=0, null=True, verbose_name='Aportes a ARL'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='incr_aport_pension',
            field=models.FloatField(default=0, null=True, verbose_name='Aportes a Pension'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='incr_aport_salud',
            field=models.FloatField(default=0, null=True, verbose_name='Aportes a Salud'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='incr_aport_vol_pension',
            field=models.FloatField(default=0, null=True, verbose_name='Aportes Voluntaios a Pension'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='incr_solida_pensional',
            field=models.FloatField(default=0, null=True, verbose_name='Solidaridad Pensional'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='re_base_grav_reten_uvt',
            field=models.FloatField(default=0, null=True, verbose_name='Valor Retención en UVT'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='re_deduc_rent_exent',
            field=models.FloatField(default=0, null=True, verbose_name='Total Deducciones + Renta Exenta'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='re_rent_exent_lab',
            field=models.FloatField(default=0, null=True, verbose_name='Tope Deducciones + Renta Exenta'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='re_total_base_grav_reten',
            field=models.FloatField(default=0, null=True, verbose_name='Total Base Gravable para Retención'),
        ),
        migrations.AddField(
            model_name='fac_especialista_detalle',
            name='re_valor_reten',
            field=models.FloatField(default=0, null=True, verbose_name='Valor Retención'),
        ),
    ]
