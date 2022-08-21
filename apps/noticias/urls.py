from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('',views.Listar, name = 'listar_noticias'),
    path('/<int:page>',views.Listar, name = 'listar_noticias'),
    path('detalles/<str:titulo>', views.Detallar, name = 'noticia_detalles')
]