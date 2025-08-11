opcao = 1
contatos = []
while opcao != 0 :
    opcao = int(input("""
        Digite uma opção:
            1 - Listar contatos
            2 - Adicionar Um contato
            3 - editar um contato
            4 - Apagar um contato
            0 - Sair
        """))
    match opcao:
        case 1:
            for c in contatos: 
                print("Nome", c['Nome'])
                print("Telefone", c['Telefone'])
        case 2: 
            nome = input("Digite o nome do seu contato: ")
            telefone = input("Digite o numero seu contato: ")
            contatos.append({"Nome": nome, "Telefone": telefone})

        case 3: 
            nome = input("Digite o nome do seu contato: ")
            for c in contatos:
                if c["Nome"] == nome:
                    telefone = input("Digite o numero seu contato: ")
                    c["Telefone"] = telefone
        case 4:
            nome = input('Digite o nome: ')
            for c in contatos:
                if c["Nome"] == nome:
                    contatos.remove(c)
        case 0: 
            break