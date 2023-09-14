#Importación de paquetes externos al proyecto
import pymysql.cursors
from werkzeug.security import generate_password_hash
import sqlalchemy as db
from datetime import datetime

class WpApiDb():
    #Conexion a la BBDD del servidor mySQL
    def connect(self):
        self.db = pymysql.connect(
            host = 'fgromano.com',
            port = 3306,
            user = 'fgromano_admin',
            passwd= '0_Castorp_0',
            db = 'fgromano_webpersonal',
            charset = 'utf8mb4',
            autocommit = True,
            cursorclass = pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    #Desconexion de la BBDD del servidor mySQL
    def disconnect(self):
        self.db.close()

    #Autenticación del usuario usando JWT-flask        
    def jwtAuth(self, username):
        sql = "SELECT * FROM fgromano_webpersonal.datos_usuario WHERE username = '"+ username +"';"
        self.cursor.execute(sql)
        Response = self.cursor.fetchone()
        return Response
    
    #Obtención de datos del usuario a partir de su ID usando JWT-flask
    def jwtId(self, ind_user):
        sql =  "SELECT * FROM fgromano_webpersonal.datos_usuario WHERE ind_usr = '"+ str(ind_user) +"';"
        self.cursor.execute(sql)
        Response = self.cursor.fetchone()
        return Response
        
    #Devuelve los datos de formación y experiencia del CV
    def sum_cv(self, year):
        date_ini = datetime.strptime(str(year) + '/01/01', "%Y/%m/%d")
        date_fin = datetime.strptime(str(year) + '/12/31', "%Y/%m/%d")
        sql = "SELECT * FROM fgromano_webpersonal.experiencia_laboral WHERE fecha_final >= '"+ str(date_ini) +"' and fecha_final <= '"+ str(date_fin) +"';"
        self.cursor.execute(sql)
        Response = self.cursor.fetchall()
        for register in Response:
            date_aux = register['fecha_inicial'].strftime("%d/%m/%Y")
            register['fecha_inicial'] = date_aux
            date_aux = register['fecha_final'].strftime("%d/%m/%Y")
            register['fecha_final'] = date_aux
        return Response
        
    #Devuelve los datos de formación del CV
    def sum_educ(self, year):
        date_ini = datetime.strptime(str(year) + '/01/01', "%Y/%m/%d")
        date_fin = datetime.strptime(str(year) + '/12/31', "%Y/%m/%d")
        sql = "SELECT * FROM fgromano_webpersonal.formacion WHERE fecha_final >= '"+ str(date_ini) +"' and fecha_final <= '"+ str(date_fin) +"';"
        self.cursor.execute(sql)
        Response = self.cursor.fetchall()
        for register in Response:
            date_aux = register['fecha_inicial'].strftime("%d/%m/%Y")
            register['fecha_inicial'] = date_aux
            date_aux = register['fecha_final'].strftime("%d/%m/%Y")
            register['fecha_final'] = date_aux
        return Response

