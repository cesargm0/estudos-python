#leia um nome e escreva ele em maiusculo, minusculo, fale quantas letras tem o nome completo, qual é e quantas letras tem o primeiro e o ultimo nome.
nome = str(input('Escreva seu nome: ')).strip()
print ('Seu nome em maiusculo é {}' .format(nome.upper()))
print ('Seu nome em minusculo é {}' .format(nome.lower()))
print ('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
nome_quebrado = nome.split()
print ('Seu primeiro nome é {} e tem {} letras, seu ultimo nome é {} e tem {} letras' .format(nome_quebrado[0], len(nome_quebrado[0]), nome_quebrado[-1], len(nome_quebrado[-1])))