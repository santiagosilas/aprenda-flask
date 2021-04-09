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
    usuario_logado = True
    
    L = ['Python 3', 'Java', 'C#', "JavaScript"]

    produtos = fake.listar_produtos()


    return render_template('test.html',
        logado = usuario_logado, 
        linguagens = L,
        produtos = produtos, 
        dicionario_usuarios = ge.usuarios,
        message = {'info': 'Página de Teste'})

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/usuario/detalhes/<nome>')
def detalhes_usuario(nome):
    return f' NOME: {nome}'