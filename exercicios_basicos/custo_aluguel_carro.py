#faça um programa que pergunte quantos dias um carro foi alugado e quantos km ele foi rodado, o dia de aluguel
#custa 60 reais e o km rodado 0,15 centavos
dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))
print('O custo total do aluguel do carro é R${:.2f}' .format(dia*60+km*0.15))