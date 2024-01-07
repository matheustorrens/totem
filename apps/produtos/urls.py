from django.urls import path
from apps.produtos.views import index, imagem, buscar, adicionar_produto, editar_produto, excluir_produto, filtro_categorias

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:item_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('adicionar-produto', adicionar_produto, name='adicionar_produto'),
    path('editar-produto/<int:item_id>', editar_produto, name='editar_produto'),
    path('excluir-produto/<int:item_id>', excluir_produto, name='excluir_produto'),                  
    path('filtro-categorias/<str:categoria>', filtro_categorias, name='filtro_categorias'),
                           
]
