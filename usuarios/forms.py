from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Andre Luiz"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        max_length=50,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):

    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Andre Luiz"
            }
        )
        
    )

    email = forms.EmailField(
        label="Email",
        max_length=200,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: seuemail@gmail.com"
            }
        )

    )
    senha_1 = forms.CharField(
        label="Senha",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="Confirme sua senha",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirme sua senha"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip() # Método para remover espaços em um input de nome
            if " " in nome:
                raise forms.ValidationError("Espaços neste campo não são permitidos.")
            else:
                return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas diferentes, tente novamente.")
            else:
                return senha_2
