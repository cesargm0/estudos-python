#faça um programa que calcule a soma de numeros impares entre 1 e o número digitado pelo usuario
x = int(input('Qual é o número impar? '))
cont = 1
soma = 0
while cont <= x:
    if cont % 2 != 0:
        soma += cont
        print (cont)
    cont += 1
print(f'A soma é igual a {soma}')