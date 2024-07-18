from django.db import models

# Create your models here.
class Producto(models.Model):
    ID = models.IntegerField(primary_key=True)
    NOMBRE = models.CharField(max_length=50)
    CATEGORIA = models.CharField(max_length=50)
    CLIENTE = models.CharField(max_length=50)
    FECHA = models.DateTimeField()
    URL = models.CharField(max_length=50)
    DESCRIPCION = models.CharField(max_length=500)
