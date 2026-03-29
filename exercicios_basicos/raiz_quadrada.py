#crie um programa que mostre um número inteiro, o seu dobro, o seu triplo e a sua raiz quadrada
import math
x=float(input('Digite um número: '))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}.' .format(x,x*2,x*3,math.sqrt (x)))