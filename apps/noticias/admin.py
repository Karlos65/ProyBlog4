from django.contrib import admin

# Register your models here.
from .models  import Noticia, Categoria, Comentario

admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Comentario)