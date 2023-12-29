from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=250)

    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categorias')

    def __str__(self):
        return self.nome
