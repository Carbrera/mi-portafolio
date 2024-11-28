# Generated by Django 4.2.16 on 2024-11-21 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('book.view', 'Puede ver los libros'), ('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Owner')]},
        ),
        migrations.AlterField(
            model_name='book',
            name='valoracion',
            field=models.IntegerField(help_text='Valoración entre 0 y 1000'),
        ),
    ]