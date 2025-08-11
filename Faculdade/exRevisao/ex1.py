filmes =[ {
      'nome': 'filme1',
      'ano':  '2017', 
      'genero': 'genero2'
  },
  {
        'nome': 'filme2',
        'ano':  '2016', 
        'genero': 'genero2'
    }]


def filtrar_filmes(filmes : list):
    filmes_filtrados = []
    opcao = int(input("Digite sua opcao 1 para ano e 2 para genero "))
    match opcao:
        case 1:
            ano_escolhido = input("Digite o ano ")
            for filme in filmes:
                if filme['ano'] == ano_escolhido:
                    filmes_filtrados.append(filme)
        case 2:
            genero_escolhido = input("Digite o genero ")
            for filme in filmes:
                if filme['genero'] == genero_escolhido:
                    filmes_filtrados.append(filme)
    
    print(filmes_filtrados)
filtrar_filmes(filmes)