# Generated by Django 4.1.1 on 2022-09-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_load_load_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='load_number',
            field=models.CharField(default='C988504', max_length=255),
        ),
    ]
