# Generated by Django 2.2.4 on 2020-03-26 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0032_auto_20200326_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='procedimiento',
            options={'ordering': ['nombre_proc']},
        ),
    ]