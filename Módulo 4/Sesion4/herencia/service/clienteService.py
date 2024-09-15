from model.cliente import Cliente

class ClienteService:
    def crear_cliente(self):
        nombre      = input('Ingrese nombre del cliente: ')
        apellido    = input('Ingrese apellido del cliente: ')
        rut         = input('Ingrese el rut del cliente: ')
        descuento   = input('Ingrese el descuento del cliente: ')

        cliente = Cliente(nombre, apellido, rut, descuento)
        print(cliente)