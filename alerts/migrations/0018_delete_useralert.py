# Generated by Django 3.2.7 on 2024-11-27 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0017_useralert'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAlert',
        ),
    ]