from django.db import models

class Produto(models.Model):
     nome = models.CharField(max_length=100, null=False, blank=False)
     legenda = models.CharField(max_length=100, null=False, blank=False)
     descricao = models.TextField(null=False, blank=False)
     item = models.CharField(max_length=100, null=False, blank=False)

     def __str__(self):
          return f"Produto [nome={self.nome}]"
