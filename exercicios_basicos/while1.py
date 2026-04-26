#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
sexo = input('Qual o seu sexo? [M/F] ').upper().strip()
while sexo not in 'MF':
    sexo = input('Digite um valor valido [M/F] ').upper().strip()
print (f'Seu sexo é {sexo}.')