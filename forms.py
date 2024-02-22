from wtforms import Form,StringField, EmailField, IntegerField, validators




class UserForm( Form ):
    nombre = StringField('nombre',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Ingresa nombre valido")])
    email = EmailField('email',[validators.Email(message="Ingresa un correo valido")])
    primerA = StringField('primerA')
    edad = IntegerField('edad')


class archivoForm(Form):
    ingles = StringField('ingles',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Ingresa una palabra")])
    espanio = StringField('espanio',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Ingresa una palabra")])
    buscar = StringField('buscar',[validators.DataRequired(message="EL campo es requerido"),validators.length(min=4,max=10,message="Que buscamos")])








