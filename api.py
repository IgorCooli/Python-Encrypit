from flask import Flask
from crypto import *



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/gerachave")
def gerar_chave_resource():
    gerar_chave()
    return "Chave gerada!"


@app.route("/encrypt/<string:text>")
def encrypt_resource(text):
    return encrypt(text)



@app.route("/decrypt/<string:text>")
def decrypt_resource(text):
    return decrypt(text)


@app.route("/renovachave")
def renovar_chave_resource():
    return renovar_chave()


@app.route("/enviachave/<string:key>")
def enviar_chave_resource(key):
    return enviar_chave(key)


app.run(port=5000, debug=True)