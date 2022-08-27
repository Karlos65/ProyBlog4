from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('',views.Evento1, name = 'listar_eventos')
]