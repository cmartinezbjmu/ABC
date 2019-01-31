from django import forms
from django.utils.translation import gettext as _
from eventos.models import Evento
from django.forms import ModelForm
from django.contrib.auth.models import User

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

class UserForm(ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual registrado.')
        return email

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales"""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las claves no coinciden.')
        return password2