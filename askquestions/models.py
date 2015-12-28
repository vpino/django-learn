# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Question(models.Model):

    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto

    def publicado_hoy(self):
        return self.fecha_publicacion.date() == timezone.now().date()
    publicado_hoy.boolean = True
    publicado_hoy.descripcion_corta = "¿Preguntado hoy?"

class Answer(models.Model):
    Pregunta = models.ForeignKey(Question)
    contenido = models.TextField()
    mejor_respuesta = models.BooleanField("Respuesta preferida", default=False)

    def __str__(self):
        return self.contenido
