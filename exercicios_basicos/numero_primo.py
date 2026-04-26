#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
elementos = 0
num = int(input('Escolha um número: '))
for x in range (1,num+1):
    if num % x == 0:
        print (f'O {num} é divisivel por {x}')
        elementos += 1
if elementos == 2:
    print('Seu número é primo')
else:
    print('Seu número não é primo')