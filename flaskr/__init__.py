from flask import Flask

def create_app (config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial_canciones.db' #creamos la bd
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #no va a grabar lo que creemos, se poneporque estamos modo diseño

    app.config['JWT_SECRET_KEY']='frase-secreta' #validez de los tokens que recibamos, utilizara para cifrar
    app.config['PROPAGATE_EXCEPTIONS']= True
    return app
