class pedidos:

    idPedido = 0
    fechaPedido = 0
    idUsuario = 0
    detalleTotal = 0


    def __init__(self, idPedido, fechaPedido, idUsuario, detalleTotal):
        self.idPedido = idPedido
        self.fechaPedido = fechaPedido
        self.idUsuario = idUsuario
        self.detalleTotal = detalleTotal

        def getidPedido(self):
            return self.idPedido
        def getfechaPedido(self):
            return self.fechaPedido
        def getidUsuario(self):
            return self.idUsuario
        def getdetalleTotal(self):
            return self.detalleTotal
        
        def setidPedido(self, idPedido):
            self.idPedido = idPedido
        
        def setfechaPedido(self, fechaPedido):
            self.fechaPedido = fechaPedido
        
        def setidUsuario(self, idUsuario):
            self.idUsuario = idUsuario
        
        def setdetalleTotal(self, detalleTotal):
            self.detalleTotal = detalleTotal

        
     

idProducto = input(int("Id Producto"))
fechaPedido = input ("Fecha de Pedido")
idUsuario = input (int("Id Usuario:"))
detalleTotal = input ("Detalle: ")

