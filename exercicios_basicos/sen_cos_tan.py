#Faça um programa que leia o valor do angulo e mostre o sen, cos e tan
import math
a=int(input('Qual é o valor do ângulo? '))
print('O sen do ângulo é {:.2f}, o cos {:.2f} e a tangente {:.2f}' .format(math.sin(math.radians(a)),math.cos(math.radians(a)),math.tan(math.radians(a))))