from django import forms
from django.utils.translation import gettext as _
from eventos.models import Evento

"""
Formulario crear eventos
"""
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'categoria', 'lugar', 'direccion', 'fecha_inicio', 'fecha_fin', 'tipo']
        labels = {
            'nombre': _("Nombre"),
            'categoria': _("Categoría"),
            'lugar': _("Lugar"),
            'direccion': _("Dirección"),
            'fecha_inicio': _("Fecha de inicio del evento"),
            'fecha_fin': _("Fecha final del evento"),
            'tipo': _("Tipo"),
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lugar'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'fecha_inicio': forms.DateInput(format=('%Y-%m-%d'),
                                                 attrs={'class': 'form-control', 'placeholder': 'yyyy-MM-dd',
                                                        'type': 'date'}),
            'fecha_fin': forms.DateInput(format=('%Y-%m-%d'),
                                                       attrs={'class': 'form-control', 'placeholder': 'yyyy-MM-dd',
                                                              'type': 'date'}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo'}),
        }