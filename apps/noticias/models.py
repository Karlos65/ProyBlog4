from django.db import models
from ..usuarios.models import Usuario

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    decripcion = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=120)
    creado = models.DateField(auto_now_add=True)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to = 'noticias',null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null = True)

    #Busca por una etiqueta en negrito, devuelve el valor entre la misma
    #En caso de no encontrarla devuelve el cuerpo acortado
    def __str__(self):
        inicio = '<span style="font-weight:bold;">'
        if self.cuerpo.find(inicio) >= 0:
            final = "</span>"
            resumen = self.cuerpo[self.cuerpo.find(inicio)+len(inicio):self.cuerpo.rfind(final)]
        else:
            resumen = self.cuerpo[0:70]+"..."
        return resumen

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)
    creado = models.DateField(auto_now_add=True)
    cuerpo = models.TextField()
    titulo = models.ForeignKey(Noticia, on_delete=models.CASCADE, null = True)

    class Meta:
        ordering = ['creado']

    def __str__(self):
        return self.cuerpo
    
