#faça um programa que leia uma informação e mostre na tela seu tipo primitivo e todas as informações sobre ela
x = str(input('Escreva algo: '))
print(type(x))
print('tem espaço?', x.isspace())
print('é um número?', x.isnumeric())
print('é um número decimal?', x.isdecimal())
print('é uma palavra?', x.isalpha())
print('está escrito em minusculo?', x.islower())