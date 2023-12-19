from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)

@app.route('/')
def header():
    return render_template('header.html', titulo='página inicial')

@app.route('/servicos')
def serviços():
    return render_template('servicos.html', titulo='serviços odontológicos')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html', titulo='equipe dentária')

@app.route('/dicas')
def dicas():
    return render_template('dicas.html', titulo='dicas dentárias')

if __name__ == '__main__':
    app.run()