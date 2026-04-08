# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
um = float(input('Qual é o valor do primeiro lado do triângulo? '))
dois = float(input('Qual é o valor do segundo lado do triângulo? '))
tres = float(input('Qual é o valor do terceiro lado do triângulo? '))
if um < dois + tres and dois < um + tres and tres < um + dois:
    print ('Esse triângulo existe')
else:
    print ('Esse triângulo não existe')