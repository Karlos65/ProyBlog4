from django.shortcuts import render

from .models import Evento, Categoria

# Create your views here.
def Evento1(request):
    #Creo el diccionario para pasar los datos al templates
    ctx = {}
    #Buscar lo que quiero de la BD
    todos = Evento.objects.all()
    # Filtrar por categoria
    if "categoria" in request.GET:
        categoria = request.GET['categoria']
        if categoria != "0":
            todos = todos.filter(categoria=categoria)
    
    #Pasarlo al template
    ctx['even'] = todos
    ctx['categorias'] = Categoria.objects.all()
    return render(request,'eventos/listar_eventos.html',ctx)