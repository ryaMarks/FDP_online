# Generated by Django 3.2.16 on 2023-09-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_onlinw_usersonline_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersonline',
            name='online',
            field=models.BooleanField(default=True),
        ),
    ]
