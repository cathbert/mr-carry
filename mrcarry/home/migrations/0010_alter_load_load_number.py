# Generated by Django 4.1.1 on 2022-09-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_load_load_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='load_number',
            field=models.CharField(max_length=100),
        ),
    ]