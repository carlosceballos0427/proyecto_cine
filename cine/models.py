from django.db import models


class Cine(models.Model):
    nombre = models.CharField(max_length=20)
    dreccion = models.CharField(max_length=100)


class Sala(models.Model):
    cine = models.ForeignKey(Cine, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=20)
    numero_asientos = models.IntegerField()


class Pelicula(models.Model):
    nombre = models.CharField(max_length=20)
    duracion = models.IntegerField()
    director = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)


class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=False)
    hora_inicio = models.DateTimeField(auto_now_add=False)
    hora_fin = models.DateTimeField(auto_now_add=False)
    valor = models.IntegerField()


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)


class Boleta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=False)
    funcion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    asientos = models.IntegerField()
    valor_boleta = models.FloatField()


    