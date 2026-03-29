#escreva um programa que leia um valor em metros e exiba convertendo de km a mm

m = float(input('Quantos metros? '))
print('{} metros em km é {}km.' .format(m, m/1000))
print('{} metros em hm é {}hm.' .format(m, m/100))
print('{} metros em dam é {}dam.' .format(m, m/10))
print('{} metros em dm é {}dm.' .format(m, m*10))
print('{} metros em cm é {}cm.' .format(m, m*100))
print('{} metros em mm é {}mm.' .format(m, m*1000))