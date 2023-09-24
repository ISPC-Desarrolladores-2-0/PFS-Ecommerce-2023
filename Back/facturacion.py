class Facturacion: 
    id_facturacion = 0
    id_cliente = 0
    nombre=""
    apellido=""
    dni=""
    direccion=""
    numero_calle=""
    localidad=""
    metodo_pago=""

    def __init__(self, id_facturacion, id_cliente, nombre, apellido, dni, direccion, numero_calle, localidad, metodo_pago):
        self.id_facturacion = id_facturacion
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.numero_calle = numero_calle
        self.localidad = localidad
        self.metodo_pago = metodo_pago

    def get_name(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_dni(self):
        return self.dni
    
    def get_direccion(self):
        return self.direccion
    
    def get_numero_calle(self):
        return self.numero_calle
    
    def get_localidad(self):
        return self.localidad
    
    def get_metodo_pago(self):
        return self.metodo_pago
    
    def get_id_facturacion(self):
        return self.id_facturacion
    
    def get_id_cliente(self):
        return self.id_cliente
        
        