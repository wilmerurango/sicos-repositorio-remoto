# Generated by Django 2.2.4 on 2020-03-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0017_auto_20200325_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='nombre_act',
            field=models.CharField(max_length=20, null=True, verbose_name='lugar del proceso donde se ubica'),
        ),
    ]
