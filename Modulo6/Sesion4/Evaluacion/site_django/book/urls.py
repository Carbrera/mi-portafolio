from django.urls import path
from . import views
from .views import IndexPageView

urlpatterns = [
    # path('', views.index, name='index'),
    # path('inicio/', views.index, name='inicio'),
    path('', IndexPageView.as_view(),name='index'),
]