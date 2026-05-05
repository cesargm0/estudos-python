#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
x = s = y = 0
while x != 999:
    x = int(input('Digite um número: '))
    if x == 999:
        break
    s += x
    y += 1
print (f'A soma dos {y} valores é {s}')