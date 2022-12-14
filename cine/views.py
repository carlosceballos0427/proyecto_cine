from cine.models import *
from rest_framework import viewsets
from cine.serializer import *


# Create your views here.

class Cine_view(viewsets.ModelViewSet):
    queryset = Cine.objects.all()
    serializer_class = Cine_serializer

class Sala_view(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = Sala_serializer

class Pelicula_view(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = Pelicula_serializer


class Funcion_view(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = Funcion_serializer

class Cliente_view(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = Cliente_serializer

class Boleta_view(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = Boleta_serializer


