# Generated by Django 4.1.7 on 2023-02-22 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_distrcit_alter_city_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Distrcit',
            new_name='District',
        ),
    ]
