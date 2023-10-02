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

        def getIdPedido(self):
            return self.idPedido
        def getFechaPedido(self):
            return self.fechaPedido
        def getIdUsuario(self):
            return self.idUsuario
        def getDetalleTotal(self):
            return self.detalleTotal
        
        def setIdPedido(self, idPedido):
            self.idPedido = idPedido

        def setFechaPedido(self, fechaPedido):
          self.fechaPedido = fechaPedido

        def setIdUsuario(self, idUsuario):
            self.idUsuario = idUsuario

        def setDetalleTotal(self, detalleTotal):
            self.detalleTotal = detalleTotal
        
     

idProducto = input(int("Id Producto"))
fechaPedido = input ("Fecha de Pedido")
idUsuario = input (int("Id Usuario:"))
detalleTotal = input ("Detalle: ")

