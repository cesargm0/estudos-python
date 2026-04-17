#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
n1 = float(input('Qual é o valor da sua primeira nota? '))
n2 = float(input('Qual é o valor da sua segunda nota? '))
nota = (n1+n1)/2
if nota >= 7:
    print('APROVADO')
elif nota >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
