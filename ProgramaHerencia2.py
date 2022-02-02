'''
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro.
Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta.
La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.

La clase PlazoFijo tendrá dos atributos propios, plazo e interés.
Tendrá un método para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar la información, datos del titular plazo, interés y total de interés.

Crear al menos un objeto de cada subclase.
'''

# Creamos la clase Cuenta
class Cuenta:
	# Inicializamos los atributos de la clase
	def __init__(self, titular, cantidad):
		self.titular = titular
		self.cantidad = cantidad
 
	# Imprimimos los datos
	def imprimir(self):
		print("Titular: ", self.titular)
		print("Cantidad: ", self.cantidad)
 
 
# Creamos la clase CajaAhorro
# Esta clase hereda atributos de la clase Cuenta
class CajaAhorro(Cuenta):
	# Iniciamos los atributos de la clase
	def __init__(self, titular, cantidad):
		super().__init__(titular, cantidad)
 
	# Imprimimos los datos de la cuenta
	def imprimir(self):
		print("Cuenta de caja de ahorros")
		super().imprimir()
 
 
# Creamos la clase PlazoFijo
# Esta clase también hereda atributos de la clase Cuenta
class PlazoFijo(Cuenta):
	# Inicializamos los atributos de la clase
	def __init__(self, titular, cantidad, plazo, interes):
		super().__init__(titular, cantidad)
		self.plazo = plazo
		self.interes = interes
 
 
	# Calculamos la ganancia
	def ganancia(self):
		ganancia = self.cantidad * self.interes / 100
		print("El importe de interés es: ", ganancia)
 
 
	# Imprimimos los resultados
	def imprimir(self):
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo disponible en días: ", self.plazo)
		print("Interés: ", self.interes)
		self.ganancia()
 
 
# Bloque principal
caja1 = CajaAhorro("Manuel", 5000)
caja1.imprimir()
 
plazo1 = PlazoFijo("Isabel", 8000, 365, 1.2)
plazo1.imprimir()