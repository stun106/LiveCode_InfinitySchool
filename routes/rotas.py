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
            return flask.redirect(flask.url_for('index'))
        aviso = {"erro":"verifique seus dados"}
        
    if len(armazenamento) > 0:
        query = armazenamento[0]
        resp = requests.get(f"https://viacep.com.br/ws/{query}/json/")
        armazenamento.clear()
        return flask.render_template("index.html",aviso = aviso, resp=resp.json())
    return flask.render_template("index.html",aviso = aviso)
    
