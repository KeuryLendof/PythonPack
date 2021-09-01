print("Mostrar dias de la semana")

nombre = input("Cual es tu nombre: ")
matricula = input("Cual es tu matricula: ")

print(nombre,  matricula, "cuando desee salir del programa presione 999")

while True:
    
    dia = int(input("Ingrese un numero del 1 al 7 : "))
    if dia == 1:
        print("Lunes")
    elif dia == 2:
        print("Martes")
    elif dia == 3:
        print("Miercoles")
    elif dia == 4:
        print("Jueves")
    elif dia == 5:
        print("Viernes")
    elif dia == 6:
        print("Sabado")
    elif dia == 7:
        print("Domingo")
    if dia > 7:
        print("El numero introduccido es incorrecto")
    if dia < 1:
        print("El numero introduccido es incorrecto")
        
    if dia == 999:
        break

print(nombre, matricula,  " espero que este programa le haiga funcionado correctamente, lo esperamos pronto")

 
        


