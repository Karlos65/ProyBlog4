from django.shortcuts import render, redirect
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

def Detallar(request):
    if request.method == "GET":
        titulo_noticia = request.GET['titulo']
        noticia = Noticia.objects.get(titulo=titulo_noticia)
        if noticia:
            ctx = {}
            ctx['notis'] = noticia
        return render(request, 'noticias/noticia_detalles.html', ctx)
    else:
        return redirect(Listar(request))
