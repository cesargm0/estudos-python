import random
print ('''Esse é o jogo da advinhação...
Pensei em um número de 0 a 100...''')
numj = int(input('Qual número escolhi? '))
num = random.randint(0,100)
chute = 1
while numj > num:
    numj = int(input('O número que escolhi foi menor, tente novamente: '))
    chute += 1
while numj < num:
    numj = int(input('O número que escolhi foi maior, tente novamente: '))
    chute += 1
if numj == num:
    print (f'Parabéns, você ecertou com {chute} tentativas, eu escolhi o {num}!')