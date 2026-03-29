#desenvolva um programa que mostre as duas notas de um aluno e calcule a média entre elas.

nota1 = float(input('Qual é a nota 1 do aluno(a)? '))
nota2 = float(input('Qual é a nota 2 do aluno(a)? '))
print('A média aritmética entre {} e {} é {}!' .format(nota1, nota2, (nota1 + nota2)/2))