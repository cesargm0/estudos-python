#crie um programa que leie o salário de um funcionario e aplique um reajuste salarial de 15%
s = float(input('Qual é o salário do funcionario? '))
print('O salário de R${:.2f} do funcionário com 15% de reajuste fica: R${:.2f}' .format(s,s*1.15))