import random

print("Generador de matricula de vehiculos dominicanos")

alphabet = "abcdefghijklmnoqkstuwxz"
numbers = "0123456789"
total_licenses = 20

for i in range(total_licenses):
    letter1 = random.choice(alphabet)
    letter2 = random.choice(alphabet)
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    num3 = random.choice(numbers)
    num4 = random.choice(numbers)
    num5 = random.choice(numbers)
    print("{}{}-{}{}{}{}{}".format(letter1,letter2,num1,num2,num3,num4,num5))
    