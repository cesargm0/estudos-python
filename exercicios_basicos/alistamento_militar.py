#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input('Qual é o seu ano de nascimento? '))
idade = 2026 - ano
print (f'Quem nasceu em {ano} tem {idade} em 2026')
if idade < 18:
    print (f'Faltam {18 - idade} anos para o seu alistamento militar.')
else:
    print (f'Você deveria ter se alistado a {idade - 18} anos atrás.')
print(f'O ano do seu alistamento foi/era/será em {ano + 18}.')