from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Evento
from eventos.forms import EventoForm
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.



def login_view(request):

    #if request.user.is_authenticated:
        #return redirect(reverse('images:index'))

    mensaje = ''

    if request.method == 'POST': #Si el usuario está enviando el formulario con datos
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('images:index'))
        else:
            mensaje = 'Nombre de usuario o clave no valido'

    return render(request, 'eventos/login.html', {'mensaje': mensaje})



class EventoCreate(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'forms/evento-form.html'
    success_url = reverse_lazy('login')