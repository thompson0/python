c = int(input('Digite a temperatura em Celsius '))
opcao = 1
while opcao:
    opcao = int(input("""
        Digite uma opção:
            1 - Celsius
            2 - Fahrenheit
            3 - Kelvin
            0 - Sair
        """))
    match opcao:
        case 1:
            print(c)
        case 2:
            f = (c * (9/5)) + 32
            print(f)
        case 3:
            k = c +273
            print(k)
        case 0:
            break