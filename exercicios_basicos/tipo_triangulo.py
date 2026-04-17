lado1 = float(input('Qual é a medida do segmento 1 do triângulo? '))
lado2 = float(input('Qual é a medida do segmento 2 do triângulo? '))
lado3 = float(input('Qual é a medida do segmento 3 do triângulo? '))
if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    if lado1 == lado2 and lado1 == lado3:
        print ('Seu triângulo é equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print ('Seu triângulo é isósceles')
    else:
        print ('Seu triângulo é escaleno')
else:
    print ('Seu triângulo não existe')
