from time import sleep as delay


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        delay(0.5)
        print(n, end=' ', flush=True)
    print(f'Foram informados {len(num)} valores ao todo.')
    ma = 0 if len(num) == 0 else max(num)
    print(f'O maior valor informado foi {ma}')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
