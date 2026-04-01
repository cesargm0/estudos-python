#Construa um algoritmo para o cálculo da menção final de APC.

presenca = float(input('Qual é a porcentagem de presença do aluno? '))
if presenca < 75:
    print('SR (Sem Rendimento)')
else:
    prova_um = float(input('Qual nota o aluno tirou na prova 1? '))
    if prova_um < 5:
        print('SR (Sem Rendimento)')
    else:
        prova_dois = float(input('Qual nota o aluno tirou na prova 2? '))
        if prova_dois < 5:
            print('SR (Sem Rendimento)')
        else:
            mpp = (prova_um + prova_dois)/2
            t = float(input('Qual nota o aluno tirou no trabalho? '))
            if t < 5:
                print('SR (Sem Rendimento)')
            else:
                mq = float(input('Qual nota o aluno tirou nos questionários? '))
                if mq < 5:
                    print('SR (Sem Rendimento)')
                else:
                    nota = mpp*0.4+t*0.3+mq*0.3
                    if nota >= 9:
                        print('SS (Superior)')
                    elif nota >= 7:
                        print('MS (Médio Superior)')
                    elif nota >= 5:
                        print('MM (Médio)')
                    elif nota >= 3:
                        print('MI (Médio Inferior)')
                    elif nota >= 0:
                        print('II (Inferior)')
                    print('Sua média ficou {:.2f}' .format(nota))


