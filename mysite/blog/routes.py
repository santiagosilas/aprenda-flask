from flask import current_app as app, render_template
from . import fake

ge = fake.GerenciarUsuarios()

@app.route('/')
@app.route('/home')
def home():
    usuario_logado = False
    L = ['Python 3', 'Java', 'C#', "JavaScript"]
    return render_template('home.html',
        logado = usuario_logado, 
        linguagens = L,
        message = {'info': 'Olá pessoal!'})

@app.route('/test')
def test():
    usuario_logado = False
    usuarios = ge.usuarios
    L = ['Python 3', 'Java', 'C#', "JavaScript"]
    return render_template('home.html',
        logado = usuario_logado, 
        linguagens = L,
        message = {'info': 'Olá pessoal!'})


