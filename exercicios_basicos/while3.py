#Crie um programa que leia dois valores e mostre um menu na tela:
import time
num1 = int(input('Escolha o primeiro número: '))
num2 = int(input('Escolha o segundo número: '))
opcao = 0
while opcao != 5:
    print('-='*20,'''
[ 1 ] soma dos dois números
[ 2 ] multiplicação dos dois números
[ 3 ] o maior entre os dois números
[ 4 ] escolher novos números
[ 5 ] sair do programa''')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
         print (f'O resultado da soma é {num1+num2}')
    if opcao == 2:
        print (f'O resultado da multiplicação é {num1*num2}')
    if opcao == 3:
        print (f'O maior número é {max(num1,num2)}')
    if opcao == 4:
        num1 = int(input('Escolha o primeiro número: '))
        num2 = int(input('Escolha o segundo número: '))
    if opcao < 1 or opcao > 5:
        print ('Escolha um número entre 1 e 5')
    time.sleep(2)
print ('=-'*20, '''
Obrigado por participar!''')