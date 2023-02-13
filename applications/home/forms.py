
from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):

    class Meta:

        model = Prueba
        fields = ('titulo','subtitulo','cantidad')


