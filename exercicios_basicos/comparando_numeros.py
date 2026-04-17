#Escreva um programa que leia dois números inteiros e compare-os.
n1 = float(input('Escolha um número: '))
n2 = float(input('Escolha outro número: '))
if n1 > n2:
    print('O primeiro valor é maior do que o segundo.')
if n2 > n1:
    print('O segundo valor é maior do que o primeiro.')
else:
    print('Os dois valores são iguais.')