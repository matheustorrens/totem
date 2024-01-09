class Cart():
    def __init__(self, request):
        self.session = request.session

        # Obter a session key se não existir
        cart = self.session.get('session_key')

        # Se o usuário for novo, criar uma session key para ele
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        
        self.cart = cart
