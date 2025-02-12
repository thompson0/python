import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza suprema', 'categoria':'Pizza','ativo':True},
                {'nome':'Cantina','categoria':'Italiano','ativo':False}]

def exibir_nome_do_progama():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1 Cadastrar restaurante')
    print('2 Listar restaurante')
    print('3 Alternar estado do restaurante')
    print('4 Sair')

def finalizar_app():
    exibir_subtitulo('Encerrando o app')

def voltar_ao_menu_principal():
    input('\nAperte Enter para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('opção invalida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastra_novo_restaurante():
    """ Essa função serve para cadastrar um novo restaurante 
        
        inputs:
        =Nome do restaurante 
        =Categoria

        Output:
        -Adiciona um novo restaurante a lista de restaurantes

    """

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurente = input('Digite o nome do restaurente que deseja cadastrar:')
    categoria = input(f'Digite a categoria do restaurente {nome_do_restaurente}:')
    dados_do_restaurante = {'nome':nome_do_restaurente, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurente} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando restaurentes')

    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante= restaurante['nome']
        categoria= restaurante['categoria']
        ativo= 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def  alternar_estado_do_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurente que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso ' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:    
        opcao_escolhida =int (input('Escolha uma opção: ')) 
        if opcao_escolhida == 1:
            cadastra_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()    
        elif opcao_escolhida == 4:
            finalizar_app()  
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_progama()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()

