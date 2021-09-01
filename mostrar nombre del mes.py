print("Mostrar nombre del mes")

nombre = input("Cual es tu nombre: ")
matricula = input("Cual es tu matricula: ")

print(nombre,  matricula, "cuando desee salir del programa presione 999")

while True:
    mes = int(input("Ingrese un numero del 1 al 12: "))
    if mes == 1:
        print("Enero")
    elif mes == 2:
        print("Febrero")
    elif mes == 3:
        print("Marzo")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print("Mayo")
    elif mes == 6:
        print("Junio")
    elif mes == 7:
        print("Julio")
    elif mes == 8:
        print("Agosto")
    elif mes == 9:
        print("Septiembre")
    elif mes == 10:
        print("Octubre")
    elif mes == 11:
        print("Noviembre")
    elif mes == 12:
        print("Diciembre")
    else:
        print("El numero introduccido no esta en el rango de 1-12")

    if mes == 999:
        break
    
print(nombre, matricula,  " espero que este programa le haiga funcionado correctamente, lo esperamos pronto")


   









