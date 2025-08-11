candidatos_brasil = [{
    'nome':'lula',
    'votos': 0
},
{
    'nome':'bolsonaro',
    'votos': 0
}]

def votacao(candidatos : list):
    votar = True
    while votar == True:
        candidato_escolhido = input('Digite o candidato ').lower()
        for candidato in candidatos_brasil:
            if candidato_escolhido == candidato['nome']:
                candidato['votos'] += 1
                print(candidato)
            if candidato_escolhido == 'fim':
                print(candidatos)
                votar = False
                break
votacao(candidatos_brasil)
        