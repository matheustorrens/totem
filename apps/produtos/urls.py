from django.urls import path
from apps.produtos.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:item_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
]
