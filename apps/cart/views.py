from django.shortcuts import render, redirect
from django.contrib import messages

def cart(request):

    if not request.user.is_authenticated:
        messages.error(request, "Logue para acessar o carrinho.")
        return redirect('login')

    return render(request,'cart/cart.html')

def cart_adicionar(request):
    pass
    # return render(request,'cart/cart_adicionar.html')

def cart_atualizar(request):
    pass
    # return render(request,'cart/cart_atualizar.html')

def cart_deletar(request):
    pass
    # return render(request,'cart/cart_deletar.html')
