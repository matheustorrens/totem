from django.shortcuts import render, get_object_or_404

from produtos.models import Produto

def index(request):
    produtos = Produto.objects.filter(exibir=True)                      # Se a variavel exibir for True, o produto vai aparecer no index, se não ele não irá aparecer
    return render(request, 'produtos/index.html', {"cards": produtos})  # Passa os itens do banco de dados para o index.html

def imagem(request, item_id):
    produto = get_object_or_404(Produto, pk=item_id)      # pk = primary key
    return render(request, 'produtos/imagem.html', {"produto": produto})

