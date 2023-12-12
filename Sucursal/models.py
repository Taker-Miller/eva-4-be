from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    apertura = models.DateField() 
    gerente = models.CharField(max_length=100) 
    fono = models.CharField(max_length=20)  
    correo = models.EmailField()  

    def __str__(self):
        return self.nombre
