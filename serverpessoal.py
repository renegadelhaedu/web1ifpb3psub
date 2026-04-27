from flask import *

#instanciar um objeto
servidor = Flask(__name__)

#definindo uma rota,
@servidor.route('/')
def mostrar_pagina_principal():
    return render_template('homepage.html')

#tem que ser igual a que vc colocou no action
@servidor.route('/verificar' , methods=['POST'])
def receber_nome():
    nome_user = request.form.get('nomeusuario')
    return f'oi {nome_user}. VOCE é gente boa'

#executando o servidor
servidor.run()

