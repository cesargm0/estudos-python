x = int(input('Digite um número: '))
cont = 0
while x >= 1:
    x = x/10
    cont += 1
print (f'Seu número tem {cont} digitos')
