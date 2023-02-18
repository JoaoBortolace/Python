from time import sleep as delay


def ajuda(text=''):
    header(f"Acessando o manual do comando '{text}'", cor='\033[44m')
    delay(1)
    print('\033[7m', end='')
    help(text)
    print('\033[m', end='')
    delay(1)


def header(text, cor='\33[m'):
    tam = len(text) + 4
    print(f'{cor}', end='')
    print('~' * tam)
    print(f'  {text}')
    print('~' * tam)
    print('\033[m', end='')


# Programa Principal
while True:
    header('SISTEMA DE AJUDA PyHELP', '\033[43m')
    delay(.3)
    resp = str(input('Função ou Biblioteca > ')).strip()
    delay(.3)
    if resp == '':
        print('\033[31mERRO! Digite alguma Função/Biblioteca para obter ajuda ou escreva fim para sair.\033[m')
    elif resp.lower() == 'fim':
        header('ATÉ LOGO!', cor='\033[41m')
        break
    else:
        ajuda(resp)
