# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso/(altura*altura)
if imc > 40:
    print('Obesidade mórbida, CUIDADO')
elif imc >= 30:
    print('Obesidade')
elif imc >= 25:
    print('Sobrepeso')
elif imc >= 18.5:
    print('Peso ideal')
else:
    print('Abaixo do peso, CUIDADO')