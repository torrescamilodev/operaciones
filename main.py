from calculadora import * 

option = input("""
Seleccione una operación
1. Suma 
2. Resta
3. Division
""")

try:
    option = int(option)
except:
    print ("valor no valido")

if option not in [1,2,3]:
    print ("Valor no valido")
    exit()

if option == 1:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Resultado:", suma(num1, num2))
elif option == 2:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Resultado:", resta(num1, num2))
elif option == 3:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        print("Resultado:", division(num1, num2))
    else:
        print("No se puede dividir entre cero")

