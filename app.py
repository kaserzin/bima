from flask import *
from db import Equipe, Partida, Chave

app = Flask(__name__)

e = Equipe
p = Partida
c = Chave

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

@app.route('/chaves')
def list_chaves():
    chaves = c.listar_chaves()
    return render_template("chaves.html", chaves=chaves)

@app.route("/chaves/novo", methods=['GET', 'POST'])
def cadastrar_chave():
    if request.method == 'POST':
        dados = request.form.to_dict()
        nova_chave_id = c.nova_chave(dados.get('nome'))
        equipes_selecionadas = request.form.getlist('equipes')
        for equipe_id in equipes_selecionadas:
            c.adicionar_equipe(nova_chave_id, int(equipe_id))
        return redirect(f'/chaves/{nova_chave_id}/equipes')
    equipes = e.listar_equipe()
    return render_template('form_chave.html', chave=None, title='Nova Chave', equipes=equipes)



@app.route("/chaves/<int:id_chave>/equipes", methods=['GET', 'POST'])
def gerenciar_equipes_chave(id_chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        id_equipe = dados.get('equipe_id')

        if id_equipe:
            c.adicionar_equipe(id_chave, int(id_equipe))
            return redirect(f'/chaves/{id_chave}/equipes')

    equipes = c.listar_equipes_chave(id_chave)
    equipes_disponiveis = c.equipes_disponiveis()
    return render_template("equipes_chave.html", equipes=equipes, chave_id=id_chave, equipes_disponiveis=equipes_disponiveis)

@app.route("/chaves/<int:id_chave>/equipes/remover/<int:id_equipe>")
def remover_equipe_chave(id_chave, id_equipe):
    c.remover_equipe(id_chave, id_equipe)
    return redirect(f'/chaves/{id_chave}/equipes')

@app.route("/chaves/<int:id>/editar", methods=['GET', 'POST'])
def editar_chave(id):
    chave = c.detalha_chave(id)
    if request.method == 'POST':
        dados = request.form.to_dict()
        c.atualiza_chave(id, dados.get('nome'))
        return redirect('/chaves')
    if chave is None:
        flash('Chave não encontrada')
        return redirect('/chaves')
    return render_template('form_chave.html', chave=chave, title='Editar Chave')

@app.route("/chaves/<int:id>/remover")
def apagar_chave(id):
    c.remove_chave(id)
    return redirect('/chaves')

if __name__ == '__main__':
    app.run(debug=True)
