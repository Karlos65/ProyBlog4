from django.shortcuts import render, redirect
from .models import Noticia, Comentario, Categoria
# Create your views here.
def Listar(request):
    #Creo el diccionario para pasar los datos al templates
    ctx = {}
    #Buscar lo que quiero de la BD
    todas = noticias = Noticia.objects.all()

    # Filtrar por categoria
    if ("categoria" in request.GET):
        categoria = request.GET['categoria']
        noticias = noticias.filter(categoria=categoria)

    # Filtrar pro autor
    if ("autor" in request.GET):
        autor = request.GET['autor']
        noticias = noticias.filter(autor=autor)

    #Pasarlo al template
    ctx['notis'] = noticias
    ctx['categorias'] = Categoria.objects.all()
    ctx['autores'] = todas.values_list('autor', flat=True).distinct

    return render(request,'noticias/listar_noticias.html',ctx)

def Detallar(request, titulo):
    if titulo:
        noticia = Noticia.objects.get(titulo=titulo)
        if noticia:
            ctx = {}
            ctx['notis'] = noticia
            comentarios = Comentario.objects.filter(titulo=noticia.id)
            if comentarios:
                ctx['coments'] = comentarios
        return render(request, 'noticias/noticia_detalles.html', ctx)
    else:
        return redirect(Listar(request))
