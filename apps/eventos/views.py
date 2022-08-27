from django.shortcuts import render

from .models import Evento

# Create your views here.
def Evento1(request):
    #Creo el diccionario para pasar los datos al templates
    ctx = {}
    #Buscar lo que quiero de la BD
    todos = Evento.objects.all()
    
    #Pasarlo al template
    ctx['even'] = todos
    
    return render(request,'eventos/listar_eventos.html',ctx)