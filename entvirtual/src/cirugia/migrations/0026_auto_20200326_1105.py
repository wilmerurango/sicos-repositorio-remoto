# Generated by Django 2.2.4 on 2020-03-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0025_auto_20200326_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canasta',
            name='presentacion',
            field=models.CharField(max_length=20, null=True, verbose_name='Presentación'),
        ),
    ]
