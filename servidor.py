from flask import *

app = Flask(__name__)

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
    if login == 'junior' and senha == '12345':
        return render_template('logado.html')
    else:
        return render_template('index5.html')


app.run()
