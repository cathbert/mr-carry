# Generated by Django 4.1.1 on 2022-09-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_load_load_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='load_number',
            field=models.CharField(default='T783281562', max_length=255),
        ),
    ]