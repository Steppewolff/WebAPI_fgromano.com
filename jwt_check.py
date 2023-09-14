#Importación de paquetes del proyecto
from user import User
import db

wp = db.WpApiDb()

#Función para comprobar usuario y pwd introducidos con la BDD
def authenticate(username, password):
    wp.connect()
    result=wp.jwtAuth(username)
    wp.disconnect()
    if result['username'] and result['pwd']==password:
        user = User(result['ind_usr'], result['username'], result['pwd'])
        return user

#Función payload para actualizar los datos del usuario de la sesion en flask_JWT    
def identity(payload):
    ind_user = payload['identity']
    wp.connect()
    result = wp.jwtId(ind_user)
    wp.disconnect()
    user = User(result['ind_usr'], result['username'], result['pwd'])
    return user