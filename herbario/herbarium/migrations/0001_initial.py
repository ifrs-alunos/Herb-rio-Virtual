# Generated by Django 2.2.2 on 2019-06-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('scientific_name', models.CharField(blank=True, max_length=200, verbose_name='Nome científico')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
            ],
        ),
    ]
