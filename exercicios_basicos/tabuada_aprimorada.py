#mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um número para saber sua tabuada: '))
for t in range (1,11):
    print (f'{num} X {t} = {num*t}')