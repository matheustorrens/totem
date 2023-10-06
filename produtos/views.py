from django.shortcuts import render, get_object_or_404

from produtos.models import Produto

def index(request):
    produtos = Produto.objects.filter(exibir=True)                      # Busca todos os itens do banco de dados
    return render(request, 'produtos/index.html', {"cards": produtos})  # Passa os itens do banco de dados para o index.html

def imagem(request, item_id):
    produto = get_object_or_404(Produto, pk=item_id)      # pk = primary key
    return render(request, 'produtos/imagem.html', {"produto": produto})

def buscar(request):
    produtos = Produto.objects.filter(exibir=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            produtos = produtos.filter(nome__icontains=nome_a_buscar)

    return render(request, "produtos/buscar.html", {"cards": produtos})

