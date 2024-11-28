from django.db import models
import datetime

# Create your models here.
# https://docs.djangoproject.com/en/5.1/topics/db/models/
# https://www.w3schools.com/django/django_models.php
class Book(models.Model):
    # atributos
    titulo = models.CharField(max_length = 100, null = False)
    autor = models.CharField(max_length = 50, null = False)
    valoracion = models.IntegerField(help_text = 'Valoración entre 0 y 1000')
    creado = models.DateTimeField(default=datetime.datetime.now())
    modificado = models.DateTimeField(default=datetime.datetime.now()) 
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        permissions = [
            ('book.view', 'Puede ver los libros'),
            ('development', 'Permiso como Desarrollador'),
            ('scrum_master', 'Permiso como Scrum Master'),
            ('product_owner', 'Permiso como Product Owner'),
            
    ]
        
    def __str__(self):
        return self.titulo