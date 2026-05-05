dias_total = int(input())
anos = dias_total // 365
resto_anos = dias_total % 365
meses = resto_anos // 30
dias = resto_anos % 30

print(f"{anos} anos, {meses} meses e {dias} dias")

if meses == 0 and dias == 0 and anos > 0:
    print("pa-pa-pa-parabensss!!!")