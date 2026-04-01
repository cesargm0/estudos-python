# Faça um algoritmo que leia a idade da pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.
# Assuma que o ano tem sempre 365 dias e o mês sempre 30 dias.

ano = int(input('Quantos anos você têm? '))
mes = int(input('Quantos meses você têm? '))
dia = int(input('Quantos dias você têm? '))
total = ano*365+mes*30+dia
print('Você já viveu {} dias.' .format(total))