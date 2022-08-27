from django.shortcuts import render

def Home(request):
	return render(request,'home.html')

def Ubicacion(request):
	return render(request,'ubicacion.html')