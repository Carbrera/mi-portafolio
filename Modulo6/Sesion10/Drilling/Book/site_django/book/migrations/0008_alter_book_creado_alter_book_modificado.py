# Generated by Django 5.1.2 on 2024-11-27 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_book_creado_alter_book_modificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='creado',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 27, 20, 46, 42, 795413)),
        ),
        migrations.AlterField(
            model_name='book',
            name='modificado',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 27, 20, 46, 42, 795413)),
        ),
    ]
