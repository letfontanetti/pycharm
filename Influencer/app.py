from flask import Flask, render_template
from flask import Flask, render_template,request,redirect, session, flash

app = Flask(__name__)
app.secret_key = ('senai')

class dadosinfluencer:
    def __init__(self,nome,plataforma,seguidores,area):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.area = area

lista = []

@app.route('/influencer')
def influencer():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('influencer.html', titulo = 'Influenciadores digitais', listainfluencer = lista)

@app.route('/cadastroinfluencer')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('cadastroinfluencer.html', titulo = 'cadastro de influencer')

@app.route('/criar', methods=['POST'])
def criar():
    if 'salvar' in request.form:
        nome = request.form['nome']
        plataforma = request.form['plataforma']
        seguidores = request.form['seguidores']
        area = request.form['area']
        obj = dadosinfluencer(nome,plataforma,seguidores,area)
        lista.append(obj)
        return redirect('/influencer')
    elif 'deslogar' in request.form:
        return redirect('/')

@app.route('/excluir/<nomeinfluencer>', methods=['GET', 'DELETE'])
def excluir(nomeinfluencer):
    for i, ifc in enumerate(lista):
        if ifc.nome == nomeinfluencer:
            lista.pop(i)
            break
    return redirect('/influencer')

@app.route('/editar/<nomeinfluencer>', methods=['GET'])
def editar(nomeinfluencer):
    for i, ifc in enumerate(lista):
        if ifc.nome == nomeinfluencer:
            return render_template('Editar.html', influencer=ifc, titulo='Alterar Influencer')

@app.route('/alterar', methods=['POST', 'PUT'])
def alterar():
    nome = request.form['nome']
    for i, ifc in enumerate(lista):
        if ifc.nome == nome:
            ifc.plataforma = request.form['plataforma']
            ifc.seguidores = request.form['seguidores']
            ifc.area = request.form['area']
    return redirect('/influencer')

@app.route('/')
def login():
    session.clear()
    return render_template('Login.html', titulo='Faça seu login')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] == 'leticia' and request.form['senha'] == '123':
        session['Usuario_Logado'] = request.form['usuario']
        flash('usuário logado com sucesso')
        return redirect('/cadastroinfluencer')
    else:
        flash('usuario não encontrado')
        return redirect('/')

if __name__ == '__main__':
    app.run()
