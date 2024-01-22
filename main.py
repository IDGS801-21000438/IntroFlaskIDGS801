from flask import Flask

app = Flask (__name__)


@app.route("/")
def index():
    return "Hola Mundo"


@app.route("/hola")
def hola():
    return "<h1>Salidos desde Holaaa</h1>"

@app.route("/saludos")
def saludo():
    return "<h1>Salidos desde Saludo</h1>"

@app.route("/clientes")
def cliente():
    return "<h1>Salidos desde Clientes</h1>"

@app.route("/empleados")
def empleado():
    return "<h1>Salidos desde Empleados</h1>"


if __name__ =="__main__":
    app.run()