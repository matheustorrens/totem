from django.shortcuts import render



def index(request):
    
    dados = {

    1: {"nome": "Coxinha",
        "legenda": "Coxinha deliciosa feita na hora"},
    2: {"nome": "Donuts",
        "legenda": "Donuts de vários sabores"}
}

    return render(request, 'produtos/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'produtos/imagem.html')

