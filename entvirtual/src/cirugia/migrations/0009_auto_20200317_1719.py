# Generated by Django 2.2.4 on 2020-03-17 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0008_auto_20200317_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_proc',
            name='cod',
        ),
        migrations.AddField(
            model_name='procedimiento',
            name='cod',
            field=models.CharField(max_length=20, null=True, verbose_name='Código'),
        ),
    ]