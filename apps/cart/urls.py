from django.urls import path
from apps.cart.views import cart, cart_adicionar, cart_atualizar, cart_deletar

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('adicionar/', cart_adicionar, name='cart_adicionar'),
    path('deletar/', cart_deletar, name='cart_deletar'),
    path('atualizar/', cart_atualizar, name='cart_atualizar'),
    
]
