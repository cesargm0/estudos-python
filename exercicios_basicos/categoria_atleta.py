#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
ano = int(input('Qual é o ano do seu nascimento? '))
idade = 2026 - ano
if idade > 25:
    print ('MASTER')
elif idade > 19:
    print ('SENIOR')
elif idade > 14:
    print ('JUNIOR')
elif idade > 9:
    print ('INFANTIL')
else:
    print ('MIRIM')