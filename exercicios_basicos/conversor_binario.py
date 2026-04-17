#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Escolha um número inteiro: '))
con = int(input('''Você quer converter seu número para:
[1] Binário
[2] Octal
[3] Hexadecimal
Digite uma opção: '''))
if con == 1:
    print(f'Seu número em binário é {bin(num)}')
elif con == 2:
    print(f'Seu número em octal é {oct(num)}')
elif con == 3:
    print(f'Seu número em hexadecimal é {hex(num)}')
else:
    print('Digite um número entre as opções')
    
    