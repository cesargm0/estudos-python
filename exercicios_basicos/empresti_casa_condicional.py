# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. O juros do emprestimo é de 50%.
casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do seu salário? '))
anos = int(input('Em quantos anos você vai pagar a casa? '))
if (casa*1.5)/(12*anos) > salario*0.3:
    print('Emprestimo negado, a prestação iria ficar R${:.2f} e o seu salário é R${:.2f}, isso excede o limite de 30%.' .format((casa*1.5)/(12*anos), salario))
else:
    print('Emprestimo aceito!')