# Generated by Django 2.2.4 on 2019-10-19 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0051_auto_20191019_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='fac_especialista',
            name='uvt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.uvt', verbose_name='Nombre Tarifa'),
        ),
    ]