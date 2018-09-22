from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    autor = models.CharField(max_length=50)
    sinopsis = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)
    genero = models.CharField(max_length=50)
    capitulos = models.IntegerField()
    image = models.ImageField(upload_to='img/', blank=True)


    def publicar(self):
        self.save()

    def __str__(self):
        return self.nombre
