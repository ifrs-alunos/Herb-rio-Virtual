# Generated by Django 3.0.2 on 2020-10-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbarium', '0026_auto_20201005_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='occorrence_regions',
            field=models.ManyToManyField(to='herbarium.Region', verbose_name='Regiões de Ocorrência'),
        ),
    ]