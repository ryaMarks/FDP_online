# Generated by Django 3.2.16 on 2023-09-07 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_usersonline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersonline',
            old_name='onlinw',
            new_name='online',
        ),
    ]
