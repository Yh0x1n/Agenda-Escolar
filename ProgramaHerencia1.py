'''
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero.
El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.

Se deberán crear dos clases, la clase cliente y la clase banco.
La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.

La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.
'''

# Creación de la clase Banco
class Banco:
	# Inicio
	def __init__(self):
		self.cliente1 = Cliente("Ivan")
		self.cliente2 = Cliente("Marcos")
		self.cliente3 = Cliente("Juan")
 
	# Función para operar
	def operacion(self):
		self.cliente1.depositar(1000)
		self.cliente2.depositar(300)
		self.cliente3.depositar(43)
		self.cliente1.extraer(400)
 
	# Función para obtener los depósitos totales
	def depositos(self):
		total = self.cliente1.devolver_cantidad() + self.cliente2.devolver_cantidad() + self.cliente3.devolver_cantidad()
		print("El total de dinero del banco es: ", total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()
 
 
 
# Creamos la clase Cliente
class Cliente:
	# Inicializamos
	def __init__(self, nombre):
		self.nombre = nombre
		self.cantidad = 0
 
	# Función para depositar dinero
	def depositar(self, cantidad):
		self.cantidad += cantidad
 
	# Función para extraer dinero
	def extraer(self, cantidad):
		self.cantidad -= cantidad
 
	# Función para obtener el total de dinero
	def devolver_cantidad(self):
		return self.cantidad
 
	# Función para imprimir los datos del cliente
	def imprimir(self):
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)
 
 
# Bloque principal
banco1 = Banco()
banco1.operacion()
banco1.depositos()