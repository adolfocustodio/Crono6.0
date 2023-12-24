from django.db import models
from categorias.models import Categoria

class Postagem(models.Model):
    titulo = models.CharField(max_length=250)
    desc = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
