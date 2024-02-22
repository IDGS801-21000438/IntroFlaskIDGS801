from flask import Flask, render_template,request,redirect
from flask import flash, g
from flask_wtf.csrf import CSRFProtect
import forms 

app = Flask (__name__)
app.secret_key = 'Inali'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.before_request
def before_request():
    g.nombre = 'Ulises'
    print('before 1')

@app.after_request
def after_reques(response):
    print('after <--->')
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/archivo", methods=['GET', 'POST'])
def archivo():
    resultado = None  
    
    if request.method == 'POST':
        if 'action' in request.form:
            if request.form['action'] == 'guardar':
                ingles = request.form['ingles']
                espanio = request.form['espanio']
                
                with open('idiomas.txt', 'a') as archivo:
                    archivo.write(f"{ingles}\n{espanio}\n")

            elif request.form['action'] == 'buscar':
                buscar = request.form['buscar']
                
                with open('idiomas.txt', 'r') as archivo:
                    palabras = archivo.read().splitlines()
                    for i in range(0, len(palabras), 1):
                        if palabras[i].lower() == buscar.lower():
                            resultado = f"La palabra '{buscar}' corresponde a '{palabras[i+1]}'."
                            break
                    else:
                        resultado = f"No se encontró una traducción para '{buscar}'."

    return render_template("archivo.html", resultado=resultado)


@app.route("/alumnos", methods= ['GET','POST'])
def alumnos():
    print('Alumnos : {}'.format(g.nombre))
    alumno_clase= forms.UserForm(request.form)
    nom = ''
    ape=''
    email=''
    edad=''
    if request.method == 'POST' and alumno_clase.validate():
       
        nom = alumno_clase.nombre.data
        ape = alumno_clase.primerA.data
        email = alumno_clase.email.data
        edad = alumno_clase.edad.data

        print("Nombre: {}".format(nom))
        print("Apellido: {}".format(ape))
        print("Email: {}".format(email))
        print("Edad: {}".format(edad))

        mensaje = 'Bienvendos {}'.format(nom)
        flash(mensaje)

    return render_template("alumnos.html",form=alumno_clase,nom=nom, primerA = ape, email = email, edad = edad )

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")


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

@app.route("/calcular",methods=["GET","POST"])
def calcular():

    if request.method=="POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1) * int(num2)))
    else:
        return '''
        <form action = "/calcular", method ="POST">
        <label>Numero 1:</label>
        <input type="text" name="n1"><br>
        <label>Numero 2:</label>
        <input type="text" name="n2"><br>
        <input type="submit "/>
        </form>
            '''
    
@app.route("/operaBas")
def operaBas():
    return render_template("operaBas.html")

@app.route("/resultado",methods=["GET","POST"])
def resultado():
    if request.method=="POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1) * int(num2)))


if __name__ =="__main__":
    app.run(debug=True)