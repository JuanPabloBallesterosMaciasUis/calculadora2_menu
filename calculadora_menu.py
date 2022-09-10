# Calculadora con menú
from math import log
from operator import truediv

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
# processing
if(opcion ==1):
    z = x + y
    print(x,"+",y)
elif (opcion ==2):
    z = x - y
    print(x,"-",y)
elif (opcion ==3):
    z = x * y
    print(x,"x",y)
elif (opcion ==4 and y!=0):
    z = x / y
    print(x,"/",y)
elif (opcion ==4 and y==0):
    print("El donominador el igual a cero y")
    print("No se puede realizar la division")
    bandera=True
elif (opcion ==5):
    z = pow(x,y)
    print(x,"^",y)
elif (opcion ==6 and x > 0):
    print("logaritmo de",x)
elif(opcion == 6 and x<=0):
    print("El valor de x es <= a cero y")
    print("No se puede calcular el logaritmo.")
    bandera = True
else:
    print ("Opcion no valida")

# se escribe el resultado con otra condicion
if (opcion < 7 and bandera==False):
    print("El resultado es",z)
