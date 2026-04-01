# Dado o salário bruto de um funcionário e a quantidade de dependentes, calcule e mostre o total de descontos, o total de
# acréscimos, e o salário líquido.

salario_bruto = float(input('Qual é o seu salário bruto? '))
dependentes = float(input('Quantos dependentes você tem? '))
salario_liquido = (salario_bruto*0.92*0.9)+(dependentes*50)
print ('O salário líquido contando com os descontos de INSS e IR mais os acréscimos de dependentes é {}' .format(salario_liquido))
1500
