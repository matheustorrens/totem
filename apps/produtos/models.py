from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Produto(models.Model):

     OPCOES_CATEGORIA = [
          ("SALGADOS", "Salgados"),
          ("DOCES", "Doces"),
          ("BEBIDAS", "Bebidas"),
     ]

     nome = models.CharField(max_length=100, null=False, blank=False)                        # O Método CharField entende apenas tuplas, como no caso das 
     legenda = models.CharField(max_length=100, null=False, blank=False)                     # OPCOES_CATEGORIAS, sendo obrigatório o seu uso, por isso o: 
     categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')      # ("SALGADOS", "Salgado") por exemplo.
     descricao = models.TextField(null=False, blank=False)
     item = models.ImageField(upload_to="itens/%Y/%m/%d/", blank=True)                       # O Blank pode ser removido depois ou usa-lo para dizer ao cliente que tal promoção acabou caso queira, ou algo do tipo, produto expirado (apenas uma ideia, caso não vá para frente, colocar blank=False)
     exibir = models.BooleanField(default=True)
     # data_produto = models.DateTimeField(default=datetime.now, blank=False)                # Define a data do produto (caso queira adicionar, lembre-se de fazer as migrações (makemigratios e migrate))
     usuario = models.ForeignKey(
          to=User,
          on_delete=models.SET_NULL,
          null=True,
          blank=False,
          related_name="user",
     )

     def __str__(self):
          return self.nome
