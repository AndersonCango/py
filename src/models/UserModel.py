from database.db import get_connection
from .entities.User import User

class UserModel:
    
    @classmethod
    def add_user(self, User):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO cliente(cedula_cli, nombre_cli, apell_cli, user_cli, pass_cli, dir_cli, tlf_cli) VALUES(%s, %s,%s,%s,%s,%s,%s)", (user.)))
                resulset = cursor.fetchall()
                
                
                    
            connection.close()
        
        except Exception as e:
            raise Exception(e)
    