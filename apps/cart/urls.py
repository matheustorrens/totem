from django.urls import path
from apps.cart.views import cart

urlpatterns = [
    path('cart', cart, name='cart'),
]
