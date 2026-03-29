#faça um programa que mostre um número e quebra ele na parte inteira

n = float(input('Digite um número com parte fracionado: '))
print('O seu número é {} e a sua parte inteira é {:.0f}' .format(n,n))

#pode fazer também usando o math.trunc()

import math
print('O seu número é {} e a sua parte inteira é {}' .format(n,math.trunc(n)))