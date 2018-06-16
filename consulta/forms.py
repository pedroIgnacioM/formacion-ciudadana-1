from django import forms
from .models import Consulta, ConsultaPropuesta, ConsultaRespuesta
from datetime import datetime
from django.forms.widgets import SelectDateWidget

class ConsultaForm(forms.ModelForm):
    '''
    Formulario para la creacion de la consulta
    '''
    titulo = forms.CharField()
    fecha_finalizacion = forms.DateField(widget=SelectDateWidget, initial=datetime.now) 
    fecha_inicio = forms.DateField(widget=SelectDateWidget, initial=datetime.now) 
    descripcion = forms.CharField(widget= forms.Textarea) 

    class Meta:
            model = Consulta
            fields = ('titulo', 'descripcion', 'fecha_inicio', 'fecha_finalizacion')


class ConsultaPropuestaForm(forms.ModelForm):
    '''
    Formulario para crear alternativas para una consulta
    '''
    titulo = forms.CharField()
    descripcion = forms.CharField(widget= forms.Textarea) 
    contenido = forms.CharField(widget= forms.Textarea) 
    class Meta:
            model = ConsultaPropuesta
            fields = ('titulo', 'descripcion', 'contenido')
