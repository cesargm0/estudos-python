#ler nomes, fazer lista, embaralhar a lista e apresentar o resultado dessa lista em ordem aleatoria

import random
x=str(input('primeiro aluno  '))
y=str(input('segundo aluno '))
n = [x,y]
random.shuffle(n)
print('A ordem de apresentação será {}' .format(n))