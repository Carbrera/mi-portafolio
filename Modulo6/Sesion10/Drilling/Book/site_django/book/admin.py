from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('titulo', 'autor', 'valoracion')
    list_filter = ('autor', 'valoracion', 'modificado')
    
admin.site.register(Book, BookAdmin)  # user: admin, pass: carlitos
