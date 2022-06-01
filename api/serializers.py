from sistema.models import (
    Secção,
    Arquivo,
    Caçifo,
    Documento
)

from rest_framework import serializers

class SeccaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secção
        fields = '__all__'

class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = '__all__'

class CacifoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caçifo
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'