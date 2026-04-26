def imc():
    altura = float(input('Qual é a sua altura (m)? '))
    peso = float(input('Qual é o seu peso (kg)? '))
    imc = peso/(altura**2)
    print (imc)
imc()