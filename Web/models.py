from django.db import models

class Fechas(models.Model):
    FECHA_CREACION = models.DateTimeField(auto_now_add=True)
    FECHA_ACTUALIZACION = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Usuario(Fechas):
    ID = models.IntegerField(primary_key=True)
    USUARIO = models.CharField(max_length=50)
    CLAVE = models.CharField(max_length=50)
    
class Persona(Fechas):
    ID_USUARIO = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE, db_column="ID_USUARIO")
    NOMBRE=models.CharField(max_length=50)
    APELLIDO=models.CharField(max_length=50)
    EMAIL=models.CharField(max_length=50)
    FECHA_NACIMIENTO = models.DateField()