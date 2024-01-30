from wtforms import Form,StringField, EmailField, TelField, IntegerField




class UserForm( Form ):
    nombre = StringField('nombre')
    email = EmailField('email')
    primerA = StringField('primerA')
    edad = IntegerField('edad')








