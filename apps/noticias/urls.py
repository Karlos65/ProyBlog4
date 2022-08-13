from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('',views.Listar, name = 'listar_noticias'),
    path('detalles/', views.Detallar, name = 'noticia_detalles')
]