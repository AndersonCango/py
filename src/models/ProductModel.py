from database.db import get_connection
from .entities.Product import Product

class ProductModel:
    
    @classmethod
    def get_products(self):
        
        try:
            connection = get_connection()
            products = []
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT cod_prod, c.nom_cat, nom_prod, img_prod, precio_venta, fecha_ven, stock FROM producto p JOIN categoria c on p.cod_cat = c.cod_cat ORDER BY stock DESC")
                resulset = cursor.fetchall()
                
                for row in resulset:
                    product = Product(row[0], row[1],row[2],row[3],row[4], row[5], row[6])
                    products.append(product.to_JSON())
                    
            connection.close()
            return products
        
        except Exception as e:
            raise Exception(e)
        
    
    @classmethod
    def get_product(self, nom_prod):
        
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT cod_prod, c.nom_cat, nom_prod, img_prod, precio_venta, fecha_ven, stock FROM producto p JOIN categoria c on p.cod_cat = c.cod_cat WHERE nom_prod = %s",(nom_prod,))
                row = cursor.fetchone()
                
                product == None
                if row != None:
                    product = Product(row[0], row[1],row[2],row[3],row[4], row[5], row[6])
                    product = product.to_JSON()
                    
            connection.close()
            return product
        
        except Exception as e:
            raise Exception(e)