# Generated by Django 5.1 on 2024-09-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
