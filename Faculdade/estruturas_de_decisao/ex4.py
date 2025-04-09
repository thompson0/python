numeros = (1,2,3)

if numeros[0] > numeros[1]:
    if numeros[0] > numeros[2]:
        maior = numeros[0]       
    else:
        maior = numeros[2]
else:
    if numeros[1] > numeros[2]:
        maior = numeros[1]
    else:
        maior = numeros[2]
  
print(maior)        
    
    