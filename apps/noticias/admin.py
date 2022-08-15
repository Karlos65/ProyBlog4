from django.contrib import admin

# Register your models here.
from .models  import Comentario, Noticia, Categoria

admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Comentario)