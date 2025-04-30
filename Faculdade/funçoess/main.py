# def saudacao(nome):
#     '''
#     Essa função imprime uma saudação personalizada.
#     '''
#     return(f'Ola, {nome} feios!')
# mensagem = saudacao('lucas')

# args= [3,5]
# resultado = somar(*args)
# print(resultado)  

# def criar_usuario(nome, idade=18, cidade="São Paulo"):
#     print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
# criar_usuario("Ana") 
# criar_usuario("Pedro", 25)
# criar_usuario("Clara", 30, "Rio de Janeiro")

# def altera_lista(lista):
#     lista.append(2)
#     lista.append(3)
#     print(lista)
    

# lista = [1,2,3,4,5]    
# altera_lista(lista[:])
# print(lista)    
    
# def soma_total(*numeros):
#     return sum(numeros)
    

# print(soma_total(1,2,3,4,5)) 
# print(soma_total(10,20,30)) 
# print(soma_total(100,200,300,400,500)) 

# def exibir_informacao(**informacoes):
#     for chave, valor in informacoes.items():
#         print(f"{chave}: {valor}")
        
# exibir_informacao(nome="Lucas", idade=25, cidade="São Paulo")
# exibir_informacao(nome="Ana", profissao="Engenheira", idade=30)        