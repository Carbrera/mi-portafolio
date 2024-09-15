from herencia import Persona
from herencia import Supervisor
from herencia import Cliente

supervisor = Supervisor('Juan', 'Perez', 123456, 'Sur')
cliente = Cliente('José', 'Sanchez', 456789, 20)


supervisor.imprimir_datos()
print("******")
supervisor.imprimir_supervisor()
print("******")
print(supervisor)
print("******")

cliente.imprimir_datos()
print("******")
cliente.imprimir_cliente()
print("******")
print(cliente)
