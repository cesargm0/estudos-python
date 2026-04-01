#Construa um algoritmo que recebe como entrada a nota final de um aluno e sua frequência nas aulas e retorna como saída a menção.

presenca = float(input('Qual é a porcentagem de presença do aluno? '))
if presenca < 75:
    print('SR (Sem Rendimento)')
else:
    nota = float(input('Qual é a nota do aluno? '))
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

                            
                