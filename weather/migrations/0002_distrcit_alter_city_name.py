# Generated by Django 4.1.7 on 2023-02-22 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distrcit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'districts',
            },
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]