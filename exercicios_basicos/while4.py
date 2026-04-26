print ('GERADOR DE PA'.center(37))
print ('=-'*20)
import time
primeiro = int(input('Qual é o primeiro termo da PA? '))
razao = int(input('Qual é a razão da PA? '))
num = int(input('Quantos termos terá sua PA? '))
times = 1
print (primeiro, end=' ---> ')
while times < num-1:
    print (primeiro + (razao * times), end=' ---> ')
    times += 1
    time.sleep(0.3)
print ((primeiro) + (razao * times))