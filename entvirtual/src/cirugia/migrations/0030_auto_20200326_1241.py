# Generated by Django 2.2.4 on 2020-03-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0029_procedimiento_uvr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedimiento',
            name='uvr',
            field=models.FloatField(blank=True, null=True, verbose_name='UVR'),
        ),
    ]