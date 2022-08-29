from django.contrib import admin
from .models  import Evento, Categoria, Modalidad
# Register your models here.
admin.site.register(Evento)
admin.site.register(Categoria)
admin.site.register(Modalidad)