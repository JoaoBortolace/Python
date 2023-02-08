from time import sleep as delay
alunos = []

while True:
    alunoNome = str(input('Nome: ')).strip()
    alunoNota = [float(input('Nota 1: ').replace(',', '.')), float(input('Nota 2: ').replace(',', '.'))]
    alunoMedia = (alunoNota[0] + alunoNota[1])/2

    aluno = [alunoNome, alunoNota, alunoMedia]
    alunos.append(aluno)

    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'N°. NOME {"MÉDIA":>15}')
print('-' * 35)

for pos, aluno in enumerate(alunos):
    print(f'{pos}{aluno[0]:>8}{aluno[2]:>15.1f}')

while True:
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if resp == 999:
        print('FINALIZANDO...')
        delay(0.65)
        print('<<< VOLTE SEMPRE >>>')
        break
    print(f'Notas de {alunos[resp][0]} são {alunos[resp][1]}')
    print('-' * 35)
