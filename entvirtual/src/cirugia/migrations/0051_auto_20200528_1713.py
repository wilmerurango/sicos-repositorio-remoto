# Generated by Django 2.2.4 on 2020-05-28 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0050_consulta_ganancia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canasta',
            name='cantidad',
            field=models.FloatField(default=1, null=True, verbose_name='Cantidad'),
        ),
    ]