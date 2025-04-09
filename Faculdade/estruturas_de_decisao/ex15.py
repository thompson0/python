estado= input("Digite o estado civil").upper()

match estado:
    case 'S':
        print('solteiro')
    case 'C':
        print('casado')
    case 'D':
        print('divorciado')
    case 'V':
        print('viuvo')
    case _:
        print('estado civil invalido')