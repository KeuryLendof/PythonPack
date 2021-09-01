x = "racecar".casefold() #casefold es para tratar mayusculas y minusculas como iguales

A = x[::-1]

if (x==A):
    print("SI! es palindroma")
else:
    print("NO! no es palindroma")


#Como saber si una frase es palindroma

x = "ali tomo tila"
x_lower = x.casefold()
x_split = x_lower.split(' ') #split sirve para juntar las palabras
x_join = ''.join(x_split)

x_A = x_join[::-1]
print(x_A)

if (x_join == x_A):
    print("Si la frase {} Es palindroma".format(x))
else:
    print("NO! la frase {} no es palindroma".format(x))
