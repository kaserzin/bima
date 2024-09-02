from flask import *
from db import Equipe, Chave

app = Flask(__name__)

e = Equipe
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


@app.route("/chaves")
def listar_chaves():
    chaves = Chave.listar_chaves()
    for chave in chaves:
        chave['equipes'] = Chave.listar_equipes_chave(chave['id'])
    return render_template('chaves.html', chaves=chaves)


@app.route("/chaves/novo", methods=["GET", "POST"])
def nova_chave():
    if request.method == "POST":
        nome_chave = request.form['nome_chave']
        equipes_selecionadas = request.form.getlist('equipes')
        nova_chave_id = Chave.nova_chave(nome_chave)
        
        for equipe_id in equipes_selecionadas:
            Chave.adicionar_equipe(nova_chave_id, equipe_id)
        
        return redirect(url_for('listar_chaves'))
    else:
        todas_equipes = Equipe.listar_equipe()
        equipes_disponiveis = [equipe for equipe in todas_equipes if Chave.equipes_disponiveis(equipe['id'])]
        return render_template('form_chave.html', equipes=equipes_disponiveis)



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


@app.route('/editar_chave/<int:id>', methods=['GET', 'POST'])
def editar_chave(id):
    if request.method == 'POST':
        pass
    else:
        chave = Chave.detalha_chave(id)
        equipes_na_chave = Chave.listar_equipes_chave(id)
        equipes_disponiveis = Chave.equipes_disponiveis()

        return render_template('editar_chave.html', title="Editar Chave", chave=chave, equipes_na_chave=equipes_na_chave, equipes_disponiveis=equipes_disponiveis)
    



@app.route("/chaves/remover/<int:id>", methods=['GET'])
def remover_chave(id):
    chave = Chave.detalha_chave(id)
    Chave.remove_chave(id)
    return redirect('/chaves')

if __name__ == '__main__':
    app.run(debug=True)
