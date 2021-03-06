from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    autor = models.CharField(max_length=50)
    sinopsis = models.CharField(max_length=364)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)
    genero = models.CharField(max_length=50)
    capitulos = models.IntegerField()
    link = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='img/', blank=True)
    imagen_portada = models.ImageField(upload_to='img/', blank=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)


    def publicar(self):
        self.save()

    def __str__(self):
        return self.nombre



class Anime(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    autor = models.CharField(max_length=50)
#    sinopsis = models.CharField(max_length=364)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=50)
    capitulos = models.IntegerField()
    link = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='img/', blank=True)
    imagen_portada = models.ImageField(upload_to='img/', blank=True)
    fecha_publicacion = models.DateField(blank=True, null=True)


    def publicar(self):
        self.save()

    def __str__(self):
        return self.nombre
