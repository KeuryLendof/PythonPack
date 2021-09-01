vocales = ("a","e","i","o","u")
user_in = input("Introduce un texto: ")
user_in = user_in.lower() #lower es para convertir mayusculas en minusculas#
new_user_in = ""
# letters es una variable nueva, el programa elimina del texto las letras que haigas introducido en la variable vocales #
for letters in user_in:
    if letters not in vocales:
        new_user_in = new_user_in + letters

print("Tu texto sin vocales es: {} ".format(new_user_in))
print(len(new_user_in)) # len es para mostrar cuantos digitos quedaron en new_user_in #
