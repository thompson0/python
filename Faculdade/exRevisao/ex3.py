opcao = 1
tarefas = []
while opcao != 0:
    opcao = int(input("""
        Digite uma opção:
            1 - Listar tarefas
            2 - Adicionar uma tarefa
            3 - editar uma tarefa
            4 - Apagar uma tarefa
            0 - Sair
        """))
    match opcao:
        case 1:
            for t in tarefas:
                print('Nome:', t['Nome'])
                print('Prioridade:', t['Prioridade'])
                print('Concluida:', t['Concluida'])
                
        case 2: 
            pass