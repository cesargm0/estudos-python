import random
maquina = random.randint(1,3)
print (('=-'*5+'JO-KEN-PO'+'-='*5).center(20))
jogador = int(input('''Qual vai ser a sua jogada?
[1] Pedra
[2] Papel
[3] Tesoura
Escolha uma das opções: '''))
if jogador >= 1 and jogador <= 3:
    if jogador == 1:
        if maquina == 1:
            print ('O Jogador escolheu pedra e a máquina escolheu pedra também, deu EMPATE')
        if maquina == 2:
            print ('O Jogador escolheu pedra e a máquina escolheu papel, você PERDEU')
        if maquina == 3:
            print ('O Jogador escolheu pedra e a máquina escolheu tesoura, você GANHOU')
    if jogador == 2:
        if maquina == 1:
            print ('O Jogador escolheu papel e a máquina escolheu pedra, você GANHOU')
        if maquina == 2:
            print ('O Jogador escolheu papel e a máquina escolheu papel, deu EMPATE')
        if maquina == 3:
            print ('O Jogador escolheu papel e a máquina escolheu tesoura, você PERDEU')
    if jogador == 3:
        if maquina == 1:
            print ('O Jogador escolheu tesoura e a máquina escolheu pedra, você PERDEU')
        if maquina == 2:
            print ('O Jogador escolheu tesoura e a máquina escolheu papel, você GANHOU')
        if maquina == 3:
            print ('O Jogador escolheu tesoura e a máquina escolheu tesoura, deu EMPATE')
else:
    print ('Escolha um número entre as opções listadas')
    