#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Qual é o seu sálario? '))
if sal > 1250:
    print ('O seu novo salário é {:.2f}' .format(sal*1.1))
else:
    print ('O seu novo salário é {:.2f}' .format(sal*1.5))