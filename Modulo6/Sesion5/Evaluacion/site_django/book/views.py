from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class IndexPageView(TemplateView): # un view o controlador con una clase
    template_name = 'navbar.html'
    
def index(request):
    return render(request,'index.html')

def navbar(request):
    return render(request, 'navbar.html')