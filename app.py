from flask import Flask, render_template, request, redirect, url_for, flash
from helpers.validacoes import validar_senha

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Lista de usuários 
users = [
    {'email': 'usuario1@example.com', 'senha': 'senha1'},
    {'email': 'usuario2@example.com', 'senha': 'senha2'}
]


# Página inicial com login
@app.route('/')
def index():
    return render_template('index.html')

# Página de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
      return render_template('cadastro.html')

    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        senha = request.form['senha']
        confirm_senha = request.form['confirm_senha']

        resultado = validar_senha(senha)

        if senha != confirm_senha:
            resultado.append('As senhas devem ser iguais')

        if resultado is True:
            return redirect('/')

        else:
            return render_template('cadastro.html', erros=resultado, nomeCompleto=nome, cpf=cpf, telefone=telefone, endereco=endereco, email=email)


    return render_template('cadastro.html')

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Verifica se o usuário existe na lista (substitua por verificação real)
        user = next((user for user in users if user['email'] == email and user['senha'] == senha), None)

        if user:
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciais inválidas. Tente novamente.', 'error')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
