import math, random, pygame
pygame.init()
pygame.mixer.music.load('Tudo_em_vao_2.mp3')
pygame.mixer.music.play()
input().event.wait()
num = float(input("Digite um numero quebrado"))
inteiro= math.floor(num)
print(inteiro)

num2=int(input('Digite um angulo'))
tangente= math.tan(math.radians(num2))
cosseno = math.cos(math.radians(num2))
seno = math.sin(math.radians(num2))
print('Tangente {:.2f}, cosseno {:.2f}, seno {:.2f}'.format(tangente,cosseno,seno))

op=float(input("Comprimento do cateto oposto"))
ad=float(input("Comprimento do cateto adjecente"))

hipot=math.hypot(op,ad)
print(hipot)

aluno1=str(input('Digite um nome de um aluno'))
aluno2=str(input('Digite um nome de um aluno'))
aluno3=str(input('Digite um nome de um aluno'))
aluno4=str(input('Digite um nome de um aluno'))
sorteado=[aluno1,aluno2,aluno3,aluno4]
penis=sorted(sorteado)
print(penis)

aluno1=str(input('Digite um nome de um aluno'))
aluno2=str(input('Digite um nome de um aluno'))
aluno3=str(input('Digite um nome de um aluno'))
aluno4=str(input('Digite um nome de um aluno'))
sorteado=[aluno1,aluno2,aluno3,aluno4]
penis=random.choices(sorteado)
print(penis)

