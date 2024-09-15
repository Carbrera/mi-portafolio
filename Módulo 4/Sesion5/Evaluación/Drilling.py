class Persona:
    def __init__(self, nombre, apellido, anio):
        self.nombre = nombre
        self.apellido = apellido
        self.anio = anio
        
class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto
        
class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anio, nombre_dpto, nombre_corto_dpto, salario):
        super().__init__(nombre, apellido, anio)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario
        
trabajador = Trabajador('Juan', 'Perez', 2005, 'Ingeniería de software', 'IS', 20000)

print(trabajador.__dict__)

print(f'Es trabajador instancia de Persona: {isinstance(trabajador, Persona)}')
print(f'Es trabajador instancia de Departamento: {isinstance(trabajador, Departamento)}')
print(f'Es trabajador instancia de Trabajador: {isinstance(trabajador, Trabajador)}')