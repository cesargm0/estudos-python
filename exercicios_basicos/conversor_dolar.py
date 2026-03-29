#faça um programa que leia quanto de dinheiro uma pessoa tem na carteira e converta o valor para dolares, 1R = 3.27US

r = float(input('Quanto de dinheiro você tem na carteira? '))
d = r/5.30
print('Com {} reais, você pode comprar {:.2f} dolares.' .format(r, d))