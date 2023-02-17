# Números por extenso
numExt = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = 's'
while resp == 's':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')

    print(f'Você digitou o número {numExt[num]}!')
    resp = str(input('Você deseja continuar, [s]im ou [n]ão: '))
