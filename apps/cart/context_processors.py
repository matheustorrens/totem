from .cart import Cart

# Criando um processador de contexto para o carrinho funcionar em outras paginas (assim como os produtos)
def cart(request):
    # Retornando os dados padrão do carrinho
    return {'cart': Cart(request)}
