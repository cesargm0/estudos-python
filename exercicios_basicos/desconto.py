#faça um programa que leia o valor de um produto e aplique um desconto de 5%
valor = float(input('Qual é o valor do produto? '))
print('O produto de valor R${:.2F} com 5% de desconto fica R${:.2F}!' .format(valor, valor*0.95))