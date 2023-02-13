from viacep_api import app
import flask
import requests

# para cada requisição de usuario o cep será armazenado aqui
armazenamento = list()
@app.route('/', methods = ["POST","GET"])
def index():
    aviso = dict()
    if flask.request.method == "POST":
        dados = flask.request.form['cep']
        if 8 == len(dados): 
            armazenamento.append(dados)
            print(armazenamento)
            return flask.redirect(flask.url_for('buscador'))
        aviso = {"erro":"verifique seus dados"}
        return flask.render_template("index.html",aviso = aviso)
            
    
    return flask.render_template("index.html",aviso = aviso)
    
@app.route('/buscador',methods =["GET","POST"])
def buscador():
    if flask.request.method == "GET":
        #onde a magica acontece, pegando a primeira posição da minha lista "armazenamento"
        query = armazenamento[0]
        print(query)
        # fazendo a requisição de acordo a instrução passada pela documentação via_api
        resp = requests.get(f"https://viacep.com.br/ws/{query}/json/")
        armazenamento.clear()
    return flask.render_template("buscador.html", resp = resp.json())    