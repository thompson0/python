numero = int(input("Digite um número: "))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")    