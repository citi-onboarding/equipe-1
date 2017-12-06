from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=50, primary_key=True)
    senha = models.CharField(min_length=6)
    telefone = models.CharField(min_length=11)
    casas = models.ManyToManyField(Casa)

class Casa(models.Model):
    titulo = models.CharField(max_length=100)
    valor = models.FloatField()
    endereco = models.CharField(max_length=140)
    data_adicao = models.DateField(auto_now=True) #vai ter argumento?
    foto = models.FileField(upload_to='') #botar o caminho da pasta onde vao ficar as imagens
    usuario = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    codigo = models.AutoField(primary_key=True)