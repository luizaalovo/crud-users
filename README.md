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


## Imagens do funcionamento do protótipo
_____________________
![image](https://github.com/luizaalovo/crud-users/assets/94422867/a5ba2ba3-0627-4d82-8fb9-dceaad4f6ac1)
_____________________
![image](https://github.com/luizaalovo/crud-users/assets/94422867/df071117-6117-4e34-89dd-5c2930aa2c0f)
_____________________
![image](https://github.com/luizaalovo/crud-users/assets/94422867/4d9fe016-2d48-4985-b796-5af78f5e20cd)
_____________________
![image](https://github.com/luizaalovo/crud-users/assets/94422867/3cac4bec-87c4-4915-a465-5eb16efa2624)
_____________________
![image](https://github.com/luizaalovo/crud-users/assets/94422867/b65f258e-ed9f-4cec-95ff-0d1825055a50)
_____________________
