from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'luiza123.'
app.config['MYSQL_DB'] = 'crud_usuarios'

mysql = MySQL(app)

@app.route('/')
def index():
    # Função para renderizar o template index.html e exibir os usuários cadastrados
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', users=data)

@app.route('/insert', methods=['POST'])
def insert():
    # Função para inserir um novo usuário no banco de dados
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        cpf = request.form['cpf']
        login = request.form.get('login')
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, cpf, login, password) VALUES (%s, %s, %s, %s)", (name, cpf, login, password))
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    # Função para deletar um usuário do banco de dados
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/update/', methods=['POST', 'GET'])
def update():
    # Função para atualizar os dados de um usuário no banco de dados
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        cpf = request.form['cpf']
        login = request.form['login']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE users SET name=%s, cpf=%s, login=%s, password=%s
        WHERE id=%s
        """, (name, cpf, login, password, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
