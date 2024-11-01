from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request): # un view o controlador mediante una función
    return HttpResponse('<h1>anita lava la tina</h1>')

class IndexPageView(TemplateView): # un view con una clase
    template_name = 'index.html'
    
def palindromo(request, palabra): # yo hago yoga hoy
    es_palindromo = ''
    
    palabra_sin_espacios = palabra.replace(' ', '')  # yohagoyogahoy
    if palabra_sin_espacios == palabra_sin_espacios[::-1] :
        es_palindromo = 'ES PALINDROMO'
    else:   # si no lo es
        es_palindromo = 'NO ES PALINDROMO'
        
    context = {'es_palindromo': es_palindromo, 'palabra': palabra}
    
    return render(request,'palindromo.html', context)