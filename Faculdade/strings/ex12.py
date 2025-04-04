palavra = 'Python é uma linguagem poderosa'
tabela= palavra.maketrans('aeiou', '     ')

print(palavra.translate(tabela))