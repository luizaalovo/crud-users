# CRUD de Usuários 📝
Este é um aplicativo simples de CRUD (Create, Read, Update, Delete) para gerenciar dados de usuários usando Python e o framework Flask com banco de dados MySQL.

## Ferramentas utilizadas
- Python
- Flask
- MySQL
- Flask-MySQLdb
- Bootstrap
- jQuery

## Instalação
1. Clone o repositório:
   ```python
   git clone https://github.com/luizaalovo/crud-users.git
   ```
2. Navegue até o diretório do projeto:
   ```python
   cd crud-users
   ```
3. Instale as dependências necessárias usando o pip:
   ```python
   pip install -r requirements.txt
   ```
4. Importe o esquema do banco de dados do arquivo ```database.sql``` para o seu servidor MySQL.
   
5. Modifique as configurações de conexão com o banco de dados no arquivo ```app.py``` para corresponder à configuração do seu servidor MySQL:
    ```python
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'sua-senha'
    app.config['MYSQL_DB'] = 'crud_usuarios'
    ```
    
## Executando o aplicativo
1. Após concluir a instalação e configurar o banco de dados, execute o seguinte comando no terminal:
    ```python
    python app.py
    ```
2. Acesse o aplicativo no seu navegador web usando o seguinte endereço:
    ```python
    [python app.py](http://localhost:5000)
    ```
    

A partir daí, você poderá cadastrar, visualizar, atualizar e excluir usuários por meio da interface fornecida.
