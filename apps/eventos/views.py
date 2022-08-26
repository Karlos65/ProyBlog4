from django.shortcuts import render

from .models import Evento

# Create your views here.
def Evento(request):
    #Creo el diccionario para pasar los datos al templates
    ctx = {}
    #Buscar lo que quiero de la BD
    todas = Evento.objects.all()
    
    #Pasarlo al template
    ctx['even'] = todas
    
    return render(request,'eventos/listar_eventos.html',ctx)