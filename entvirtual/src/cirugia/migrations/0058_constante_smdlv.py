# Generated by Django 2.2.4 on 2020-06-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0057_procedimiento_dias_estancia'),
    ]

    operations = [
        migrations.AddField(
            model_name='constante',
            name='smdlv',
            field=models.FloatField(default=0, null=True, verbose_name='Salaraio Minimo Diario L.V.'),
        ),
    ]