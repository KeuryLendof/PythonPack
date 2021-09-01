user_input = str(input("Introduzca su gmail: "))
print("Su gmail es: {}".format(user_input))

user_name = user_input[:user_input.index("@")]
domain_name = user_input[user_input.index("@")+ 1:]

print("Su nombre de usuario es: {} | Su dominio es: {}".format(user_name, domain_name))


# Otra forma con partition este lo que hace es que separa por mitad

email = str(input("introduzca su email: "))

partes = email.partition("@")

print("Tu nombre es: {}".format(partes[0]))
print("Tu dominio es: {}".format(partes[2]))
