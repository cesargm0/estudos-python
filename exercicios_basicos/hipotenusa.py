#Faça um programa que leia os catetos e dê o valor da hipotenusa

c1 = float(input('Qual o valor do cateto 1? '))
c2 = float(input('Qual o valor do cateto 2? '))
import math
print('O valor da hipotenusa é {:.2f}' .format(math.hypot(c1,c2)))