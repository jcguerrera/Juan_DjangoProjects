from django.db import models
import uuid
# Create your models here.

class Hygrometer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Participante(models.Model):
    codigo = models.IntegerField(verbose_name='codigo')
    nombre = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length=30)
    tipoIndicador = models.CharField(max_length = 30)
    prioridad = models.IntegerField(verbose_name='prioridad')