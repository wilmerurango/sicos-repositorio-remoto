# Generated by Django 2.2.4 on 2020-03-02 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0161_auto_20200302_0938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='cpp_proveedor',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre']},
        ),
    ]
