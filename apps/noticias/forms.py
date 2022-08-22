from django import forms
from .models import Comentario

class FormularioComentar(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('cuerpo',)
