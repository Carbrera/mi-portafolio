from django.urls import path
from . import views
from .views import IndexPageView, index, navbar

urlpatterns = [
    path('', IndexPageView.as_view(), name='navbar'),
    path('index/', index, name='index'),
    path('navbar/', navbar, name='navbar')
]