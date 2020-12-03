# naner_bicho
No arquivo seetings DEFAULT_FROM_EMAIL = 'seu_email@gmail.com' #coloque seu email aqui SECRET_KEY = 'secret_key' #o django gera uma chave aleatoria quando cria o projeto(depois faço um passo a passo como fazer funcionar)

DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': os.environ.get('DB_NAME', 'nome_do_bd'), #coloque o nome do banco de dados, do PostgreSQL (se quiser trabalhar com esse banco de dados lógico) 'USER': os.environ.get('DB_USER', 'usuario_db'), #coloque o usuario 'PASSWORD': os.environ.get('DB_PASS','senha_db'), #coloque a senha 'HOST':'localhost', 'PORT': '5432', } }

![alt text](https://github.com/LUCASRENAA/naner_bicho/blob/main/static/imagens/imagem_site_bixo.jpg?raw=true)
Esse é o site que desenvolvi como projeto do certificado(que vai ser exibido), aprendi a fazer todos os processos de uma criação de um sistema, back-end com Python(Django) e PostgreSQL, e o front-end com HTML,CSS e Bootstrap.



![alt text](https://github.com/LUCASRENAA/naner_bicho/blob/main/static/imagens/certificado.png?raw=true)


![alt text](https://github.com/LUCASRENAA/naner_bicho/blob/main/static/imagens/certificado_html_web_developer.jpg?raw=true)


![alt text](https://github.com/LUCASRENAA/naner_bicho/blob/main/static/imagens/certificado_postgresql.jpg?raw=true)