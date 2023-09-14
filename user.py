#Clase que almacena los datos del usuario para flask_JWT en la sesión
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        
    def __str__(self):
        return f"User ID: {self.id}"