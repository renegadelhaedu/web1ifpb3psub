from flask import *
from usuario import Usuario
app = Flask(__name__)

usuarios = []
@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/excluirusuarios')
def excluirusuarios():
    return 'ok', 200

@app.route('/listar')
def listar_usuarios():
    return render_template('listar.html', usuarios=usuarios)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    novo_usuario = Usuario(nome, email, senha)
    usuarios.append(novo_usuario)
    return render_template('home.html')

app.run()
