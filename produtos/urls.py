from django.urls import path
from produtos.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem/', imagem, name='imagem'),
]