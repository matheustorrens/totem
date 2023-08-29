from django.shortcuts import render

def index(request):
    return render(request, 'produtos/index.html')

def imagem(request):
    return render(request, 'produtos/imagem.html')

