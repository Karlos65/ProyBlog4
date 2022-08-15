from django.shortcuts import render
from .models import Noticia
# Create your views here.
def Listar(request):
    #Creo el diccionario para pasar los datos al templates
    ctx = {}
    #Buscar lo que quiero de la BD
    todas = Noticia.objects.all()
    
    #Pasarlo al template
    ctx['notis'] = todas
    
    
    return render(request,'noticias/listar_noticias.html',ctx)