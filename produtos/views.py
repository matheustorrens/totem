from django.shortcuts import render, get_object_or_404

from produtos.models import Produto

def index(request):
    produtos = Produto.objects.all()    
    return render(request, 'produtos/index.html', {"cards": produtos})  # Passa todos os itens do banco de dados para o index.html

def imagem(request, item_id):
    produto = get_object_or_404(Produto, pk=item_id)      # pk = primary key
    return render(request, 'produtos/imagem.html', {"produto": produto})

