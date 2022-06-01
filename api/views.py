from django.shortcuts import render
from sistema.models import (
    Arquivo,
    Documento,
    Caçifo,
    Secção
)

from .serializers import (
    ArquivoSerializer,
    CacifoSerializer,
    DocumentoSerializer,
    SeccaoSerializer
)
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers

# Create your views here.
class ArquivoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArquivoSerializer
    queryset = Arquivo.objects.all()

class CacifoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CacifoSerializer
    queryset = Caçifo.objects.all()

class DocumentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DocumentoSerializer
    queryset = Documento.objects.all()

class SeccaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SeccaoSerializer
    queryset = Secção.objects.all()
