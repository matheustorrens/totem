from django.shortcuts import render, get_object_or_404, redirect
    
from apps.produtos.models import Produto
from apps.produtos.forms import ProdutoForms

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')

    produtos = Produto.objects.filter(exibir=True)                      # Busca todos os itens do banco de dados
    return render(request, 'produtos/index.html', {"cards": produtos})  # Passa os itens do banco de dados para o index.html

def imagem(request, item_id):
    produto = get_object_or_404(Produto, pk=item_id)      # pk = primary key
    return render(request, 'produtos/imagem.html', {"produto": produto})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado.")
        return redirect('login')

    produtos = Produto.objects.filter(exibir=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            produtos = produtos.filter(nome__icontains=nome_a_buscar)

    return render(request, "produtos/buscar.html", {"cards": produtos})

def adicionar_produto(request):
    if not request.user.is_superuser:
        messages.error(request, "Apenas administradores podem acessar esa opção.")
        return redirect('login')

    form = ProdutoForms
    if request.method == 'POST':
        form = ProdutoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto adicionado com sucesso.')

    return render(request, 'produtos/adicionar_produto.html', {'form': form})

def editar_produto(request):
    pass

def excluir_produto(request):
    pass