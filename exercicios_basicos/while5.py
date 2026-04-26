print('-'*40)
print('Sequência de Fibonnaci'.center(39))
print('-'*40)
termos = int(input('Quantos termos você quer mostrar? '))
x1 = 0
x2 = 1
quant = 1
while quant <= termos:
    fibo = x1 + x2
    x1 = x2
    x2 = fibo
    quant += 1
    print (fibo, end=' --> ')