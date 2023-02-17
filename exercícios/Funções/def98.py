from time import sleep as delay


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if (inicio > fim and passo > 0) or (inicio <= fim and passo < 0):
        passo *= -1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    delay(2)
    fim_c = fim + 1 if inicio <= fim else fim - 1
    for i in range(inicio, fim_c, passo):
        delay(0.5)
        print(i, end=' ', flush=True)
    print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
end = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, end, pas)
