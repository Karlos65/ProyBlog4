from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    decripcion = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.nombre

class Modalidad(models.Model):
    nombre = models.CharField(max_length=60)
    def __str__(self):
        return self.nombre
    
class Evento(models.Model):
    titulo = models.CharField(max_length=120)
    creado = models.DateField(auto_now_add=True)
    lugar = models.CharField(max_length=120)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to = 'eventos',null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null = True)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.titulo
    
    