#veja se o nome da cidade termina com santos

x = str(input('Qual cidade? ')).strip()
print (x[-5:].upper() == 'SANTO')
