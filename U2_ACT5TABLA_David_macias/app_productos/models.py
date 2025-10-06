from django.db import models

# Create your models here.

class Producto(models.Model): # Por convención, las clases de modelo suelen ser en singular y con la primera letra en mayúscula
    nombre = models.CharField(max_length=100, help_text="Nombre del producto")
    costo = models.IntegerField(help_text="Costo unitario del producto") # La 'I' de IntegerField en mayúscula

    def __str__(self): # Doble guion bajo antes y después de str
        return f"{self.nombre} (Costo: {self.costo})" # He añadido un formato un poco más descriptivo