from django.shortcuts import render

# Create your views here.
def Evento(request):
    return render(request, 'eventos/listar_eventos.html')