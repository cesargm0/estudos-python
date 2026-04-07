#faça um programa que leia se tem Silva no nome de alguém

nome = str(input('Qual é o seu nome completo? ')).strip()
print ('Existe "Silva" no seu nome? {}' .format('SILVA' in nome.upper()))