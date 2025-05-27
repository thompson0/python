import random

Mapa = [
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12
]

opcao = int(input('Digite Qual Opção Você Deseja \n1 - Jogar \n2 - Sair\n'))
continuar = True

enchente = random.randint(0, 11)
print(enchente)

if opcao == 1:
    start = int(input('Você quer começar aonde (1 a 12): '))
    posicao_atual = start - 1
    

    def andar_para_direita(posicao):
        if posicao % 4 != 3:
            return posicao + 1
        else:
            print("Você não pode ir mais para a direita.")
            return posicao

    def andar_para_esquerda(posicao):
        if posicao % 4 != 0:
            return posicao - 1
        else:
            print("Você não pode ir mais para a esquerda.")
            return posicao

    def andar_para_cima(posicao):
        if posicao < 4:
            print('Você não pode ir mais para cima.')
            return posicao
        else:
            return posicao - 4

    def andar_para_baixo(posicao):
        if posicao >= 8:
            print('Você não pode ir mais para baixo.')
            return posicao
        else:
            return posicao + 4

    def mostrar_mapa(posicao):
        for i in range(len(Mapa)):
            if i == posicao:
                print('[P]', end=' ')
            else:
                print(f'{Mapa[i]:2}', end=' ')
            if (i + 1) % 4 == 0:
                print()

    while continuar:
        mostrar_mapa(posicao_atual)
        print(f'\nVocê está na posição {Mapa[posicao_atual]}')

        movimento = int(input("\n1 - Esquerda | 2 - Direita | 3 - Cima | 4 - Baixo | 0 - Sair\n"))
        if movimento == 1:
            posicao_atual = andar_para_esquerda(posicao_atual)
        elif movimento == 2:
            posicao_atual = andar_para_direita(posicao_atual)
        elif movimento == 3:
            posicao_atual = andar_para_cima(posicao_atual)
        elif movimento == 4:
            posicao_atual = andar_para_baixo(posicao_atual)
        elif movimento == 0:
            continuar = False

        else:
            print("Opção inválida.")
