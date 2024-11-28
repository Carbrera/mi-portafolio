from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('titulo', 'autor', 'valoracion', 'rating')
    list_filter = ('autor', 'valoracion', 'modificado')
    
    def rating(self, obj):
        if obj.valoracion < 1000:
            return 'baja'
        elif obj.valoracion > 2500:
            return 'alta'
        else:
            return 'media'
    
admin.site.register(Book, BookAdmin)  # user: admin, pass: carlitos
