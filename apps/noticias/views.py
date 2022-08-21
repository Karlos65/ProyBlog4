from django.shortcuts import render, redirect
from .models import Noticia, Comentario, Categoria
# Create your views here.

#Meses
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre',
         'Noviembre', 'Diciembre']

def Listar(request):
    #Creo el diccionario para pasar los datos al templates
    ctx = {}
    #Buscar lo que quiero de la BD
    todas = noticias = Noticia.objects.all()

    # Filtrar por categoria
    if "categoria" in request.GET:
        categoria = request.GET['categoria']
        noticias = noticias.filter(categoria=categoria)

    # Filtrar por autor
    if "autor" in request.GET:
        autor = request.GET['autor']
        noticias = noticias.filter(autor=autor)

    # Filtrar por Anio
    if "anio" in request.GET:
        anio = request.GET['anio']
        noticias = noticias.filter(creado__year=anio)

    # Filtrar por mes
    if "mes" in request.GET:
        mes = request.GET['mes']
        if mes != "0":
            noticias = noticias.filter(creado__month=mes)

    #Pasarlo al template
    ctx['notis'] = noticias
    ctx['categorias'] = Categoria.objects.all()
    ctx['autores'] = todas.values_list('autor', flat=True).distinct
    ctx['anios'] = todas.values_list('creado__year', flat=True).distinct
    ctx['meses'] = meses

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
