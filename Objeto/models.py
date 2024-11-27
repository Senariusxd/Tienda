from django.db import models
from PIL import Image as PILImage  # Importa Pillow para manipular imágenes
import os

class Generos(models.Model):
    id = models.AutoField(primary_key=True)  # AUTO INCREMENT
    nombre = models.CharField(max_length=100)  # Ajusta el tamaño según sea necesario

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)  # AUTO INCREMENT
    nombre = models.CharField(max_length=100)  # PRIMARY KEY
    descripcion = models.TextField()  # Para texto más largo
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Ajusta según tus necesidades
    foto = models.ImageField(upload_to='productos/')  # Para imágenes
    generos = models.ForeignKey(Generos, on_delete=models.CASCADE, related_name='productos')  # Relación

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.foto:
            # Abre la imagen
            img = PILImage.open(self.foto)
            # Redimensiona la imagen
            img = img.resize((300, 300), PILImage.LANCZOS)

            # Guarda la imagen redimensionada
            img.save(self.foto.path)

        super(Producto, self).save(*args, **kwargs)