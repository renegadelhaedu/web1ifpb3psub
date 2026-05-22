from flask import *
import utils

app = Flask(__name__)
lista_usuarios = []
#recurso padrão, definir a rota /
@app.route('/')
def home_page():
    return render_template('index5.html')

#criando outra rota na minha aplicação
@app.route('/login' , methods=['POST'])
def login():
    #estou capturando campos do input que vieram do html
    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')
    if utils.verificar_login(login, senha, lista_usuarios):
        return render_template('logado.html')
    else:
        msg = 'usuário ou senha incorretos'
        return render_template('index5.html', texto=msg)

@app.route('/menuadmin')
def menuadmin():
    return render_template('menuiframe.html')

@app.route('/listar')
def listar():
    return render_template('listar.html')

app.run()
