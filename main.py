from flask import Flask, render_template

app = Flask (__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hola")
def hola():
    return "<h1>Salidos desde Holaaa</h1>"

@app.route("/saludos")
def saludo():
    return "<h1>Salidos desde Saludo</h1>"

@app.route("/nombre/<string:nombre>")
def nombre(nombre):
    return "Hola: "+nombre

@app.route("/numero/<string:numero>")
def numero(numero):
    return "Este es el numero:  " + str(numero)

@app.route("/user/<string:id>/<string:nom>")
def user(id,nom):
    return "Bienvenido Usuario" + nom + " " + id

@app.route("/suma/<string:num1>/<string:num2>")
def suma(num1,num2):
    total = int(num1) + int(num2)
    return "La suma de" + str(num1) + " " + str(num2) + " es igual a: " + str(total) 




if __name__ =="__main__":
    app.run(debug=True)