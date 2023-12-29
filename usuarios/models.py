from django.contrib.auth.models import AbstractUser
from django.db import models
from categorias.models import Categoria

class Usuario(AbstractUser):
    nome = models.CharField(max_length=250)
    first_name = None
    last_name = None

class Administrador(Usuario):
    class Meta:
        verbose_name = ('Administrador')
        verbose_name_plural = ('Administradores')

class Aluno(Usuario):
    bio = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='imagens', null=True, blank=True)

    class Meta:
        verbose_name = ('Aluno')
        verbose_name_plural = ('Alunos')

class Professor(Aluno):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = ('Professor')
        verbose_name_plural = ('Professores')
