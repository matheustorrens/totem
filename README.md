# COMO INICIAR O PROJETO:
#### </> Em uma pasta, clique com o botão direito do mouse e abra o terminal do seu sistema operacional, com o terminal aberto, utilize o comando: *git clone https://github.com/matheustorrens/totem*
#### </> Abra a pasta na sua IDE
#### </> No terminal, digite: *virtualenv {nome da venv}*, no meu caso utilizei o nome venv. (pip install virtualenv, caso não tenha)
#### </> Ainda no terminal, ative a venv com o comando: *venv/scripts/activate* (p/ windows) 
#### </> Agora, instale as bibliotecas com o comando: *pip install -r requirements.txt*
#### </> Com as bibliotecas instaladas, utilize o comando: *python manage.py migrate* e depois *python manage.py runserver*

# Social Google Auth Login:
#### </> Crie um superuser
#### </> No admin do Django, clique em "Aplicativos sociais"
#### </> Adicione um provedor
#### </> Coloque qualquer nome ex: Google Auth
#### </> Coloque o ID do cliente (Ache o id do cliente no site: https://console.cloud.google.com/)
#### </> Coloque sua chave secreta
#### </> em "sites" no Admin do Django, Selecione e passe o "example.com" para o outro lado
#### </> Depois de salvar, na sessão "sites", clique em "example.com" (nome do dominio)
#### </> Em Nome do domínio: localhost:8000
#### </> Em Nome para exibição: local
