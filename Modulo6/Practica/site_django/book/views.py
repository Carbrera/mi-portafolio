from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Bienvenido a mi sitio de libros')