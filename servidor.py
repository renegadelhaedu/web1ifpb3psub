from flask import *
import utils

#controle de sessão
app = Flask(__name__)
app.secret_key = 'JH%K$Jh55fsPd'


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
    #if utils.verificar_login(login, senha, lista_usuarios):
    if login == 'admin' and senha == '123':
        #criando um usuário na sessão
        session['usuario'] = login
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


@app.route('/listartodos')
def listartodos():
    if 'usuario' in session:
        usuarios = ['rene','josue','andre','marilia','junior']
        return render_template('listartodos.html', usuarios=usuarios)
    else:
        msg = 'precisa fazer login'
        return render_template('index5.html', texto=msg)


@app.route('/logout')
def logout():
    #remova do dicionário session o usuário logado
    session.pop('usuario',None)
    return render_template('index5.html')



app.run()

