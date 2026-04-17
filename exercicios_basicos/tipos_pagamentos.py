# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
valor = float(input('Qual é o valor das compras? '))
pagamento = int(input('''Opções de pagamento:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
Escolha uma dessas opções: '''))
if pagamento == 1:
    print (f'O valor de sua compra terá um desconto de 10%, ficando no total R${valor*0.9}')
elif pagamento == 2:
    print (f'O valor de sua compra terá um desconto de 5%, ficando no total R${valor*0.95}')
elif pagamento == 3:
    print (f'O valor de sua compra será de R${valor}, com as parcelas custando R${valor/2}')
elif pagamento == 4:
    parcelas = int(input('Você irá parcelas em quantas vezes a compra? '))
    if parcelas < 3:
        print('O número de parcelas tem que ser pelo menos em 3x nessa opção de pagamento')
    else:
        print(f'O valor de sua compra terá um juros de 20%, ficando no total R${valor*1.2}, com parcelas de R${(valor*1.2)/parcelas}')
else:
    print ('Digite o valor de uma das opções sugeridas')
    