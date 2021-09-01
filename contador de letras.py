print("Contador de letras")
print("Contar cuantas veces se repite una letra en un texto o mensaje")

user = str(input("Introduzca su texto: ")).lower()
coun = str(input("Ingreza la letra que quieres contar: ")).lower()

contador = user.count(coun)

print("Tu mensaje original es: {}".format(user))
print("Your message has {}{}'s in it!!!".format(str(coun),coun))
