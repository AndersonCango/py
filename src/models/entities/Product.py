from utils.DateFormat import DateFormat

class Product:
    
    def __init__(self, cod_prod, nom_cat, nom_prod, img_prod, precio_venta, fecha_ven, stock) -> None:
        self.cod_prod = cod_prod
        self.nom_cat = nom_cat
        self.nom_prod = nom_prod
        self.img_prod = img_prod
        self.precio_venta = precio_venta
        self.fecha_ven = fecha_ven
        self.stock = stock
        
        
    def to_JSON(self):
        return{
            'id' : self.cod_prod,
            'title_cat' : self.nom_cat,
            'tittle_prod' : self.nom_prod,
            'img_prod' : self.img_prod,
            'price' : self.precio_venta,
            'date_ven' : DateFormat.convert_date(self.fecha_ven),
            'stock' : self.stock
        }