from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Secção(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    codename = models.CharField(max_length=10, unique=True)
    descrição = models.CharField(max_length=150, blank=True)
    modificador = models.CharField(max_length=150)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)

    def __str__(self):
        return self.codename

    class Meta:
        verbose_name_plural = 'Secções'

class Caçifo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    codename = models.CharField(max_length=10, unique=True, editable=False)
    descrição = models.CharField(max_length=150, blank=True)
    secção = models.ForeignKey(Secção, on_delete=models.CASCADE)
    modificador = models.CharField(max_length=150)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)

    def __str__(self):
        return self.codename

    class Meta:
        verbose_name_plural = 'Caçifos'

class Arquivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    codename = models.CharField(max_length=10, unique=True, editable=False)
    descrição = models.CharField(max_length=150, blank=True)
    caçifo = models.ForeignKey(Caçifo, on_delete=models.CASCADE)
    modificador = models.CharField(max_length=150)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)

    def __str__(self):
        return self.codename
    
    class Meta:
        verbose_name_plural = 'Arquivos'

class Documento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    nome = models.CharField(max_length=200, unique=True)
    file = models.FileField(max_length=200, null=True, upload_to='documents/%d/%m/%Y')
    arquivo = models.ForeignKey(Arquivo, on_delete=models.CASCADE)
    modificador = models.CharField(max_length=150)
    adicionado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Documentos'
    