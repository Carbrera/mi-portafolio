crear la carpeta templates
>book/templates/

proceder a crear nuestro archivo index.html
>book/templates/index.html
* html:5

adecuar la vista views.py
> crear en book/views.py
´´´
class IndexPageView(TemplateView):
    template_name = 'index.html'
    ´´´
    
