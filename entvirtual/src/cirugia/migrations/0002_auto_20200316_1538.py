# Generated by Django 2.2.4 on 2020-03-16 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiempo_procedimiento',
            old_name='nombre_procedimiento',
            new_name='nombre_proc',
        ),
    ]
