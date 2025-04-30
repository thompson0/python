quantidade_de_termos = int(input("Quantos termos você quer mostrar? "))
primeiro_termo = 0
segundo_termo = 1
fibonacci = [primeiro_termo, segundo_termo]

for i in range(2, quantidade_de_termos):
        proximo_termo = primeiro_termo + segundo_termo
        fibonacci.append(proximo_termo)
        primeiro_termo = segundo_termo
        segundo_termo = proximo_termo
        print(fibonacci)   