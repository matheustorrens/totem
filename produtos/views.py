from django.shortcuts import render

from produtos.models import Produto

def index(request):
    produtos = Produto.objects.all()    
    return render(request, 'produtos/index.html', {"cards": produtos})  # Passa todos os itens do banco de dados para o index.html

def imagem(request):
    return render(request, 'produtos/imagem.html')

