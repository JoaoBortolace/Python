from time import sleep as delay


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    final = fim + 1 if inicio < fim else fim - 1
    for i in range(inicio, final, passo):
        delay(0.5)
        print(i, end=' ')
    print('FIM!')


def lin():
    print('-=' * 30)


# Programa Principal
lin()
contador(1, 10, 1)
lin()
contador(10, 0, -2)
lin()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
end = int(input('Fim: '))
pas = int(input('Passo: '))
lin()

pa = 1 if pas == 0 else pas
if ini > end and pa > 0:
    pa *= -1
contador(ini, end, pa)
