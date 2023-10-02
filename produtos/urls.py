from django.urls import path
from produtos.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:item_id>', imagem, name='imagem'),
]
