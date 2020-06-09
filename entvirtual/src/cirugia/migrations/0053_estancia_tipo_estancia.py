# Generated by Django 2.2.4 on 2020-05-29 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0052_delete_rubro'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_estancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_est', models.CharField(max_length=60, null=True, verbose_name='Tipo de Estancia')),
                ('numero_camas', models.IntegerField(default=0, null=True, verbose_name='Número de Camas')),
            ],
        ),
        migrations.CreateModel(
            name='estancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto_estancia', models.CharField(max_length=40, null=True, verbose_name='Concepto Estancia')),
                ('valor_concepto', models.FloatField(default=0, null=True, verbose_name='Valor día')),
                ('tipo_estancia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cirugia.tipo_estancia', verbose_name='Tipo de Estancia')),
            ],
        ),
    ]
