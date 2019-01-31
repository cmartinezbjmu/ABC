from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

"""
Modelo de evento
"""
class Evento(models.Model):
    CATEGORY_TYPES = (
        ('A', 'Conferencia'),
        ('B', 'Seminario'),
        ('C', 'Congreso'),
        ('D', 'Curso'),
    )
    TYPES_EVENT = (
        ('A', 'Presencial'),
        ('B', 'Virtual'),
    )
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=1, choices=CATEGORY_TYPES)
    lugar = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fecha_inicio = models.DateField(blank=True, null=True, default=datetime.now)
    fecha_fin = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=TYPES_EVENT)
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "evento"
        verbose_name_plural = "eventos"
        ordering = ['fecha_inicio']
