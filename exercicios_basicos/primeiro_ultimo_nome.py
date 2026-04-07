#leia o primeiro e o ultimo nome da pessoa
nome = str(input('Qual é o seu nome? ')).strip().split()
print ('Seja bem vindo(a) {} {}' .format(nome[0],nome[-1]))