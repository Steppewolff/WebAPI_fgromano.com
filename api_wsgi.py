#Importación de paquetes externos al proyecto
from flask import Flask
from flask_restful import Api, Resource
# import requests
from flask_jwt import JWT, jwt_required, current_identity
import logging
from flask_cors import CORS
import flask_http_middleware
import datetime

#Importación de paquetes del proyecto
import db
from jwt_check import authenticate, identity

#Bloque para configurar el logger de Python, en el directorio Top: Python_debug.log
logger = logging.getLogger('Python_Log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('Python_debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
# logger.debug('Debug Message')
# logger.info('Info Message')
# logger.warning('Warning')
# logger.error('Error Occured')
# logger.critical('Critical Error')

#Se crea la instancia de la API
server = Flask(__name__)
server.config['SECRET_KEY'] = 'fernandokey'
api_wp = Api(server)

wp = db.WpApiDb()

#Se implementa un JWT para gestionar accesos
jwt = JWT(server, authenticate, identity)

#Funciones para querys en la BDD
class resumee(Resource):
    @jwt_required()
    def get(self, year):
        wp.connect()
        result = wp.sum_cv(year)
        wp.disconnect()
                
        return result
    
    @server.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Access-Control-Allow-Origin')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        
        return response

class education(Resource):
    @jwt_required()
    def get(self, year):
        wp.connect()
        result = wp.sum_educ(year)
        wp.disconnect()
                
        return result
    
    @server.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Access-Control-Allow-Origin')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        
        return response

#Configuración de endpoints de la API    
api_wp.add_resource(resumee,'/resumee/<int:year>') #GET devuelve los eventos de experiencia laboral del año solicitado
api_wp.add_resource(education,'/education/<int:year>') #GET devuelve los eventos de formación del año solicitado

#Lanzamiento del programa (en servidor local/en servidor remoto), se deja comentada la que no se use
#if __name__ == '__main__':
#    server.run(debug=True)
application = server