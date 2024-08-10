#flask siempre utiliza el app.py para que sea el inicial

from flaskr import create_app
from flaskr.vistas.vistas import VistaSignIn
from .modelos import db, Cancion, Usuario, Album, Medio, AlbumSchema, CancionSchema, UsuarioSchema
from flask_restful import Api
from .vistas import *
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push() #consistente en todos los modulos, guardar los datos iniciales
#Para correrlo ingresamos en la terminal a la carpeta flaskr y luego flask run

db.init_app(app)
db.create_all() #se crean todas las clases en la bd

api = Api (app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/album/<int:id_album>/canciones')

jwt = JWTManager(app)

#prueba
""" 
with app.app_context():
    #seliarizacion, representación json de las instancias de la bd
    album_schema=AlbumSchema()
    a = Album (titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    db.session.add(a)
    db.session.commit()
    #print([album_schema.dumps(album) for album in Album.query.all()])
    
    cancion_schema=CancionSchema()
    c = Cancion(titulo='prueba', minutos=2, segundos=45, interprete='xxxxxx')
    c2 = Cancion(titulo='prueba', minutos=2, segundos=45, interprete='yyyyy')
    db.session.add(c)
    db.session.add(c2)
    db.session.commit()
    #print([cancion_schema.dumps(cancion) for cancion in Cancion.query.all()])
    
    
    usuario_schema=UsuarioSchema()
    u = Usuario (nombre='Juan', contrasena='12345')
    db.session.add(u)
    db.session.commit()
    #print([usuario_schema.dumps(usuario) for usuario in Usuario.query.all()])

    u = Usuario (nombre='Juan', contrasena='12345')
    u.albumes.append(a)
    db.session.add(u)
    db.session.commit()
    print (Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    c = Cancion(titulo='prueba', minutos=2, segundos=45, interprete='xxxxxx')
    c2 = Cancion(titulo='prueba', minutos=2, segundos=45, interprete='yyyyy')
    a.canciones.append(c)

    
    db.session.add(c)
    db.session.add(c2)
    db.session.commit()
    
    print(Cancion.query.all())
    print(Album.query.all()[0].canciones)
 """
    