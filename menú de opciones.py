print("Menu de opciones para realizar operaciones")

print("Escoja el tipo de operacion que desea realizar: ")
print("[ 1 ] Suma")
print("[ 2 ] Resta")
print("[ 3 ] Multiplicacion")
print("[ 4 ] Division")
print("Presione [ 9 ] cuando desee salir")
nombre = input("Antes de empezar nos gustaria saber su nombre: ")

while True:
    
    seleccion = int(input("Escoja su seleccion [1, 2, 3, o 4]: "))

    if seleccion == 1:
        
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = (num1 + num2)

        print("El resultado de la suma es: ", resultado)

    elif seleccion == 2:
        
         num1 = int(input("Ingrese el primer numero: "))
         num2 = int(input("Ingrese el segundo numero: "))
         resultado = (num1 - num2)

         print("El resultado de la resta es: ", resultado)

    elif seleccion == 3:

         num1 = int(input("Ingrese el primer numero: "))
         num2 = int(input("Ingrese el segundo numero: "))
         resultado = (num1 * num2)

         print("El resultado de la multiplicacion es: ", resultado)

    elif seleccion == 4:

         num1 = int(input("Ingrese el primer numero: "))
         num2 = int(input("Ingrese el segundo numero: "))
         resultado = (num1 / num2)

         print("El resultado de la division es: ", resultado)

    if seleccion == 9:
        break

print(nombre, " Espero que le haiga sido de utilidad, tenga un feliz resto del dia")

         







         
