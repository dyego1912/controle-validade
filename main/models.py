from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Importa o módulo responsável por retornar o url reverso

# Create your models here.

class Filial(models.Model):
    #id automático
    nome = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    
    class Meta:
        verbose_name_plural = 'Filiais'
        ordering = ['nome']

    def __str__(self):
        return str(self.nome)

class Funcionario(models.Model):
    usuario = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE) # Chave estrangeira para o perfil, usando o model User default
    filial = models.ForeignKey(Filial, default = 1, related_name='filial_funcionario', on_delete=models.CASCADE)
    cargo = models.CharField(max_length=20)
    #slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['usuario']
    
    def __str__(self):
        return str(self.usuario)
  
class Corredor(models.Model):
    #id automático
    nome = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    descricao = models.CharField(max_length=50)
    filial = models.ForeignKey(Filial, default = 1, related_name='filial_corredor', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Corredores'
        ordering = ['nome']
    
    def __str__(self):
        filial = str(self.filial)
        corredor = str(self.nome)
        return str(filial + ' - '+ corredor)

class Categoria(models.Model):
    #id automático
    descricao = models.CharField(max_length=255,unique=True)
    
    class Meta:
        ordering = ['descricao']
        
    def __str__(self):
        return self.descricao

class Produto(models.Model):
    #id automático
    codigo = models.IntegerField(unique=True)
    codigo_barras = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=255, unique=False)
    preco_venda = models.DecimalField(decimal_places=2, max_digits=6)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'Produtos'

    def __str__(self):

        # Sempre que printar o id do objeto, irá retornar codigo_barras + descricao

        cod = str(self.codigo_barras)
        desc = self.descricao
        return str(cod + ' - ' + desc)

    def get_absolute_url(self):
        #app_name:nome_do_url, kwargs = {"campo_bd":"self.campo_bd"}
        return reverse("main:detalhes_produtos", kwargs={"slug": self.slug})
   

class Conferencia(models.Model):
    #id automático
    funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)
    corredor = models.ForeignKey(Corredor, on_delete = models.CASCADE)
    data_conferencia = models.DateField(auto_now_add=True)

    def __str__(self):
        cod = str(self.id)
        data = str(self.data_conferencia)
        return str(cod + ' - '+data)

    def get_absolute_url(self):
        return reverse("main:detalhes_conferencia", kwargs={"id": self.id})

class Validade_Produto(models.Model):
    #id automático
    conferencia = models.ForeignKey(Conferencia, on_delete = models.CASCADE, unique=False)
    codigo_barras = models.ForeignKey(Produto, on_delete=models.CASCADE, unique=False)
    data_validade = models.DateField(unique=False)
    quantidade = models.IntegerField()
    
    '''
    def get_absolute_url(self):
        return reverse("main/detalhes_conferencia", kwargs={"id": self.id})
    '''