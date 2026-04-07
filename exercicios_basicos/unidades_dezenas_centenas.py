#faça um programa que mostre a unidade, dezena, centena e milhar de um número
num = str(input('Escreva um número: ')).strip()
nump = num.rjust(4,'0')
espaço = ' '.join(nump)
separador = espaço.split()
print ('Unidade {}' .format(separador[-1]))
print ('Dezena {}' .format(separador[-2]))
print ('Centena {}' .format(separador[-3]))
print ('Milhares {}' .format(separador[-4]))