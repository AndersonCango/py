class User:
    
    def __init__(self, cedula_cli, nombre_cli, apell_cli, user_cli, pass_cli, dir_cli, tlf_cli):
        self.cedula_cli = cedula_cli
        self.nombre_cli = nombre_cli
        self.apell_cli = apell_cli
        self.user_cli = user_cli
        self.pass_cli = pass_cli
        self.dir_cli = dir_cli
        self.tlf_cli = tlf_cli
        
    def to_JSON(self):
        return{
            'id': self.cedula_cli,
            'name_cli': self.nombre_cli,
            'lastname_cli': self.apell_cli,
            'user_cli': self.user_cli,
            'dir_cli': self.dir_cli,
            'tlf_cli': self.tlf_cli
        }