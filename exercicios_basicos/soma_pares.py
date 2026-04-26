#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
inicial = int(input('Qual é o primeiro termo da progressão? '))
razao = int(input('Qual é a razão da progressão? '))
for x in range (inicial,(inicial+(10*razao)),razao):
    print (x, end = ' ')