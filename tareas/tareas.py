from celery import Celery

#guardar el log de un logueo en la aplicación

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task() #que la funcion va a pasar a traves de la cola es necesario el decoartor
def registrar_log(usuario, fecha):
    with open('log_signin.txt', 'a+') as file: #a para crear lineas + crear  el archivo si no existe
        file.write('{} - inicio de sesion: {} \n'.format(usuario, fecha))
        