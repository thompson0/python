nome= input('qual seu nome')
print('Prazer em te conhecer {:=>20}!'.format(nome))
n1=int(input('Digite um numero'))
n2=int(input('Digite outro numero'))
print('A soma vale {}'.format(n1+n2))
print('A subtracao vale {}'.format(n1-n2))
print('A divisao vale {}'.format(n1/n2))
print('A multipliacao vale {}'.format(n1*n2))
print('A potencia vale {}'.format(n1**n2))

#Desafio 1
v1=int(input('Digite um valor '))
ant=v1-1
suc=v1+1
print('O antecessor {} o sucessor e {}'.format(ant,suc))
#Desafio2
m1=int(input('Digite um numero'))
ti=m1*3
do=m1*2
raz=m1**1/2
print('O dobro desse numero e {} o tiplo desse numero e {} a raiz desse numero e {}'.format(do,ti,raz))
#Desafio3
ac1=int(input('Digite uma nota'))
ac2=int(input('Digite sua outra nota'))
m= (ac1+ac2)/2
print('Sua media e {}'.format(m))
#Desafio4
metros=int(input('Digite uma quantia em metro'))
cm=metros*100
milimetros=cm*10
print('Sua conversao de metros para cm fica {} e para milimetros fica {}'.format(cm,milimetros))
#esafio5
t1=int(input('Digite um numeor e veja sua tabuada'))
tabuado=t1*1, t1*2, t1*3, t1*4, t1*5, t1*6, t1*7, t1*8, t1*9, t1*10
print('Sua tabuada ficou {}'.format(tabuado))
#Desafio6
cart=int(input('Digite quanto voce tem na carteira'))
dolar=cart/5.14
print('Voce pode comprar {} dolare(s)'.format(dolar))
#Desafio7


#Desafio8
produto=float(input('Digite o valor do seu produto'))
desconto=produto/5
preco=produto-desconto
print('Seu produto com desconto ficou {}R$ ele teve desconto de {}R$'.format(preco,desconto))
#Desafio9
salario=float(input('Digite seu salario'))
aumento=salario*0.15
print('Seu novo salario ficou {}'.format(aumento))

#Desafio10
larg= float(input('largura da parede '))
altu= float(input('altura da parede'))
area=larg*altu
print('Sua parede tem a dimensao de {}x{} e sua area e de {}m2'.format(larg,altu,area))
tinta= area/2
print('Para pinta essa parede voce vai precisar de {} Litro de tinta' .format(tinta))