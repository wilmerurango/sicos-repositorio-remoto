# Generated by Django 2.2.4 on 2020-03-30 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0034_remove_honorario_duracion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='honorario',
            name='uvr',
        ),
    ]