# Generated by Django 3.2.10 on 2022-04-22 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atapp', '0023_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='dashuser',
        ),
    ]
