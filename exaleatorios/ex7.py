vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input("Digite uma palavra: ")
numeroDeVogais = 0
for letra in palavra :
    if letra in vogais:
        numeroDeVogais += 1
        print(numeroDeVogais)