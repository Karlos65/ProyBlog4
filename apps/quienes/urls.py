from django.urls import path
from . import views

app_name = 'quienes'

urlpatterns = [
    path('quienes/',views.Quienes, name = 'quienes_somos'),
]