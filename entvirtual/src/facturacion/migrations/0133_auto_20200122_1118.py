# Generated by Django 2.2.4 on 2020-01-22 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0132_auto_20200113_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='serv_public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=15, null=True, verbose_name='NIT')),
                ('nombre_tercero', models.CharField(max_length=50, null=True, verbose_name='Nombre Tercero')),
                ('nombre_serv', models.CharField(max_length=50, null=True, verbose_name='Nombre Servicio')),
                ('direccion', models.CharField(max_length=50, null=True, verbose_name='Dirección')),
                ('tel', models.CharField(max_length=50, null=True, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='E-mail')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
            ],
        ),
        migrations.RemoveField(
            model_name='cuenta_aux',
            name='cuenta',
        ),
        migrations.RemoveField(
            model_name='cuenta_aux',
            name='naturaleza_cuenta',
        ),
        migrations.RemoveField(
            model_name='cuenta_aux',
            name='proveedor',
        ),
        migrations.AddField(
            model_name='cuenta_aux',
            name='num_cuenta',
            field=models.CharField(max_length=20, null=True, verbose_name='Número Cuenta'),
        ),
        migrations.AlterField(
            model_name='cuenta_aux',
            name='name_cuenta',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre Cuenta'),
        ),
        migrations.CreateModel(
            name='distri_serv_public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cuenta_especific', models.CharField(max_length=50, null=True, verbose_name='Nombre Cuenta Especifica')),
                ('num_cuenta_especific', models.CharField(max_length=50, null=True, verbose_name='Número Cuenta Especifica')),
                ('distri', models.FloatField(default=0, null=True, verbose_name='Disctribución (%)')),
                ('fecha_distri', models.DateField(null=True, verbose_name='Fecha')),
                ('centro_costo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_costo', verbose_name='Centro de Costo')),
                ('serv_public', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.serv_public', verbose_name='Nombre del Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='cpp_serv_public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.FloatField(default=0, null=True, verbose_name='Costo')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
                ('serv_public', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.serv_public', verbose_name='Nombre del Servicio')),
            ],
        ),
        migrations.AddField(
            model_name='cuenta_aux',
            name='serv_public',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.serv_public', verbose_name='Nombre del servicio'),
        ),
    ]
