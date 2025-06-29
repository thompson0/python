import math
import random

numeroAleatorio = math.floor(random.uniform(1, 100))
tentivas = 3

while (tentivas > 0):
    numero = int(input("Digite um número entre 1 e 100: "))
    if numero == numeroAleatorio:
        print("Você acertou!")
        break
    else:
        tentivas = tentivas - 1
        print("numero errado")
