# Generated by Django 2.2.4 on 2020-03-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0028_auto_20200326_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedimiento',
            name='uvr',
            field=models.FloatField(null=True, verbose_name='UVR'),
        ),
    ]