from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('evento/', views.Evento, name = 'listar_eventos'),
]