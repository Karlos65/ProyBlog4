from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=120)
    creado = models.DateField(auto_now_add=True)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to = 'eventos',null=True, blank=True)
        
    def __str__(self):
        return self.titulo