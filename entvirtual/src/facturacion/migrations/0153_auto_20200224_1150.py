# Generated by Django 2.2.4 on 2020-02-24 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0152_cpp_proveedor_detalle_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fac_especialista',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='distribucion',
            name='centro_costo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_costo', verbose_name='Centro de Costo'),
        ),
    ]
