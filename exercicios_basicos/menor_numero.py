#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
um = float(input('Qual é o valor um? '))
dois = float(input('Qual é o valor dois? '))
tres = float(input('Qual é o valor tres? '))
if um<dois<tres:
    print(um, 'é o menor número!')
elif dois<um<tres:
    print(dois, 'é o menor número!')
else:
    print(tres, 'é o menor número!')