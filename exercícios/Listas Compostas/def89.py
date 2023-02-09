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
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for pos, aluno in enumerate(alunos):
    print(f'{pos:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    resp = int(input('Mostrar notas de qual aluno? \033[1;36m(999 interrompe)\033[m '))
    if resp == 999:
        print('FINALIZANDO...')
        delay(0.65)
        print('<<< VOLTE SEMPRE >>>')
        break
    if resp <= len(alunos) - 1:
        print(f'Notas de {alunos[resp][0]} são {alunos[resp][1]}')
        print('-' * 35)
    else:
        print('\033[1;31mOpção inválida! Tente novamente\033[m')
