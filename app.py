from flask import *
from db import Equipe, Partida

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui' 

e = Equipe
p = Partida

@app.route('/')
def list_equipes():
    equipes = e.listar_equipe()
    return render_template("equipes.html", equipes=equipes)

@app.route("/equipes/remover/<int:id>")
def apagar_equipe(id):
    e.remove_equipe(id)
    return redirect('/')

@app.route("/equipes/novo", methods=['GET', 'POST'])
def cadastrar_equipe():
    if request.method == 'POST':
        dados = request.form.to_dict()
        e.novo_equipe(dados.get('nome'), dados.get('representante'))
        return redirect('/')
    return render_template('form_equipe.html', equipe=None, title='Nova Equipe')


@app.route("/equipes/editar/<int:id>", methods=['GET', 'POST'])
def editar_equipe(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        e.atualiza_equipe(id, dados.get('nome'), dados.get('representante'))
        return redirect('/')
    equipe = e.detalha_equipe(id)
    if equipe is None:
        flash('Equipe não encontrada')
        return redirect('/')
    return render_template('form_equipe.html', equipe=equipe, title='Editar Equipe')

@app.route('/partidas')
def list_partidas():
    partidas = p.listar_partidas()
    return render_template("partidas.html", partidas=partidas)

@app.route("/partidas/remover/<int:id>")
def apagar_partida(id):
    p.remove_partida(id)
    return redirect('/partidas')

@app.route("/partidas/novo", methods=['GET', 'POST'])
def cadastrar_partida():    
    if request.method == 'POST':
        dados = request.form.to_dict()
        p.nova_partida(dados.get('data'), dados.get('local'))
        return redirect('/partidas')
    return render_template('form_partida.html', partida=None, title='Nova Partida')

@app.route("/partidas/editar/<int:id>", methods=['GET', 'POST'])
def editar_partida(id):
    if request.method == 'POST':
        dados = request.form.to_dict()
        p.atualiza_partida(id, dados.get('data'), dados.get('local'))
        return redirect('/partidas')
    partida = p.detalha_partida(id)
    return render_template('form_partida.html', partida=partida, title='Editar Partida')


if __name__ == '__main__':
    app.run(debug=True)
