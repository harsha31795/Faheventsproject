# Generated by Django 3.2.10 on 2022-04-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atapp', '0032_alter_book_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='plate',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
