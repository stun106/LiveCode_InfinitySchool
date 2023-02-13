from flask import Flask

'''
render_template, request, redirect, url_for

DO MODULO flask IMPORTE A CLASSE Flask, onde usarei as funções:
-> render_template, para renderizar minhas paginas html localizadas na pasta templates;
-> redirect, para redirecionar o usuario a uma nova pagana atravez do url_for
-> url_for, tambem responsavel por linkar funções de rota para uma ação de formulario,
ou seja determinarei se a requisição http/https sera metodos do verbo post ou get de acordo a cada função.
'''

app = Flask(__name__)



from routes.rotas import *


if __name__ == "__main__":
    app.run(debug = True)