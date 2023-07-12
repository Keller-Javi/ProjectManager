from django.db import models

from django.contrib.auth.models import User # un modelo de usuario creado por django

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True) # Se añade la fecha al momento de crear la instancia
    date_completed = models.DateTimeField(null=True)
    favorite = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Se crea una relacion con el usuario que lo creo, y si este usuario se elimina se elimina sus proyectos

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    state = models.IntegerField(default=0) # State en 0 (por defecto) es que está en estado de espera, 1 es que se está haciendo y 2 es que la tarea esta completada
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
