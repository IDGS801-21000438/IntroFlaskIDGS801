from wtforms import Form,StringField, TelField



class UserForm( Form ):
    nombre = StringField('nombre')
    email = StringField('email')
    primerA = StringField('primerA')






