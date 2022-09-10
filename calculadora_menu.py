# Calculadora con menú
from math import log

print("-------------------------")
print("---CALCULADORA-MENU------")
print("-------------------------")

# input
bandera = False
x = float(input("Dame el valor del numero x: "))
y = float (input("Dame el valor del numero y: "))

print("\nDame la opcion que desea realizar: \n")
#se despliega el menu para seleccionar la opcion que deseas realizar: 
print("1. Sumar(El primero mas el segundo)")
print("2. Restar(El primero menor el segundo)")
print("3. Multiplicar(El primero por el segundo)")
print("4. Dividir(El primero sobre el segundo)")
print("5. Potencia(El primero a la potencia del el segundo)")
print("6. Logaritmo(El logartimo del primero)")

opcion = int(input("\nDame la opcion: "))