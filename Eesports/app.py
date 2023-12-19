from flask import Flask, render_template
from flask import Flask, render_template,request,redirect,session,flash

app = Flask(__name__)
app.secret_key = ('senaisp')

class dadosjogadores:
    def __init__(self,nome,jogo,funcao,ranking):
        self.nome = nome
        self.jogo = jogo
        self.funcao = funcao
        self.ranking = ranking

lista = []

@app.route('/jogadores')
def jogaderes():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('jogadores.html', titulo ='Jogadores de eSports', listajogadores = lista)

@app.route('/cadastroesports')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('cadastroesports.html', titulo ='cadastro de jogadores')

@app.route('/criar', methods=['POST'])
def criar():
    if 'salvar' in request.form:
        nome = request.form['nome']
        jogo = request.form['jogo']
        funcao = request.form['funcao']
        ranking = request.form['ranking']
        obj = dadosjogadores(nome,jogo,funcao,ranking)
        lista.append(obj)
        return redirect('/jogadores')
    elif 'deslogar' in request.form:
        return redirect('/')

@app.route('/excluir/<nomejogadores>', methods=['GET', 'DELETE'])
def excluir(nomejogadores):
    for i, jgd in enumerate(lista):
        if jgd.nome == nomejogadores:
            lista.pop(i)
            break
    return redirect('/jogadores')

@app.route('/editar/<nomejogadores>', methods=['GET'])
def editar(nomejogadores):
    for i, jgd in enumerate(lista):
        if jgd.nome == nomejogadores:
            return render_template('Editar.html', jogadores=jgd, titulo='Alterar Jogador')

@app.route('/alterar', methods=['POST', 'PUT'])
def alterar():
    nome = request.form['nome']
    for i, jgd in enumerate(lista):
        if jgd.nome == nome:
            jgd.jogo = request.form['jogo']
            jgd.funcao = request.form['funcao']
            jgd.ranking = request.form['ranking']
    return redirect('/jogadores')

@app.route('/')
def login():
    session.clear()
    return render_template('Login.html', titulo='Faça seu login')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] == 'leticia' and request.form['senha'] == '123':
        session['Usuario_Logado'] = request.form['usuario']
        flash('usuário logado com sucesso')
        return redirect('/cadastro')
    else:
        flash('usuario não encontrado')
        return redirect('/login')

if __name__ == '__main__':
    app.run()
