from django.contrib import admin

from apps.produtos.models import Produto

class ListandoProdutos(admin.ModelAdmin):                       # Classe que vai definir as funcionalidades do Django Admin

    list_display = ("id", "nome", "preco", "legenda", "exibir")          # Define o que vai ser mostrado na lista dos produtos
    list_display_links = ("id", "nome")                         # Define os campos que serão links
    search_fields = ("nome",)                                   # Função que busca pelo nome dos produtos
    list_filter = ("categoria","usuario")                       # Função que define uma lista que contem todas as categorias para filtra-las
    list_editable = ("exibir",)
    list_per_page = 10                                          # Define a quantidade de itens que serão exibidos por página
    

admin.site.register(Produto, ListandoProdutos)                  # Sempre que surgir uma nova classe, tem que coloca-la aqui
