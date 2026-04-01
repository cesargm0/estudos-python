# Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno.

nota_um = float(input('Qual é a primeira nota do aluno? '))
nota_dois = float(input('Qual é a segunda nota do aluno? '))
nota_tres = float(input('Qual é a terceira nota do aluno? '))
final = (nota_um*1+nota_dois*2+nota_tres*3)/(1+2+3)
print('A nota final do aluno é {}' .format(final))