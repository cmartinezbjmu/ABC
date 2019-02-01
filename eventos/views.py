from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Evento
from .forms import UserForm
from eventos.forms import EventoForm
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def login_view(request):
    mensaje = ''

    if request.method == 'POST': #Si el usuario está enviando el formulario con datos
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('eventos:index'))
        else:
            mensaje = 'Nombre de usuario o clave no valido'

    return render(request, 'eventos/login.html', {'mensaje': mensaje})

def add_user_view(request):
    if request.method == 'POST': #Si el usuario está enviando el formulario con datos
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            email = cleaned_data.get('email')
            password = cleaned_data.get('password')

            user_model = User.objects.create_user(username=username, password=password)
            user_model.email = email
            user_model.save()

            return HttpResponseRedirect(reverse('eventos:login'))
    else:
        form = UserForm()
    context = {
        'form': form
    }

    return render(request, 'eventos/registro.html', context)

def EventoCreate(request):
    if request.method == 'POST': #Si el usuario está enviando el formulario con datos
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            new_evento=Evento(nombre=request.POST['nombre'],
                categoria = request.POST['categoria'],
                lugar = request.POST['lugar'],
                direccion = request.POST['direccion'],
                fecha_inicio=request.POST['fecha_inicio'],
                fecha_fin=request.POST['fecha_fin'],
                tipo = request.POST['tipo'],
                usuario=request.user);
            new_evento.save() # Guardar los datos en la base de datos

            return HttpResponseRedirect(reverse('eventos:index'))
    else:
        form = EventoForm()

    return render(request, 'forms/evento-form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('eventos:login'))


def logged(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('eventos:index'))
    else:
        return login(request)

"""
Vista de eventos
"""
class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/evento_list.html'
    paginate_by = 50


class EventoDetailView(DetailView):
    model = Evento
    template_name = 'eventos/evento_detail.html'
