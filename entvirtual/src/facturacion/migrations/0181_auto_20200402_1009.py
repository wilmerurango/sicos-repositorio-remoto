# Generated by Django 2.2.4 on 2020-04-02 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0180_auto_20200313_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cpp_arriendo',
            options={'ordering': ['-id']},
        ),
    ]