# Generated by Django 5.1.2 on 2024-11-27 01:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='creado',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='modificado',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
