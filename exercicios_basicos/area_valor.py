#faça um programa que calcule a área da parede e depois calcula a quantidade de tinta para pintar, para cada 2m²
#precisa de 1 L de tinta
h = float(input('Qual a altura da sua parede? '))
c = float(input('Qual o comprimento da sua parede? '))
print('A área da sua parede é {}m² e para pinta-la irá precisar de {} litros de tinta.' .format(h*c, h*c/2))