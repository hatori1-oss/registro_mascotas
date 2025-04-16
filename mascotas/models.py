from django.db import models
from django.contrib.auth.models import User
from django.db import models
import uuid

class Mascota(models.Model):
    id_unico = models.UUIDField(default=uuid.uuid4, editable = False, unique = True)
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)  # perro, gato, etc.
    raza = models.CharField(max_length=100, blank=True)
    edad = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='mascotas/', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

