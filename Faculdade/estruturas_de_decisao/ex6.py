strings = ['A','Bb','Caa']

if len(strings[0]) > len(strings[1]):
    if len(strings[0]) > len(strings[2]):
        maior = strings[0]
        
    if len(strings[1]) > len(strings[0]):
        if len(strings[1]) > len(strings[2]):
            maior = strings[1]
else:
    maior = strings[2]            

print(maior)