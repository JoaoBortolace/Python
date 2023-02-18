

def ajuda(text):
    return 0


def header(text):
    tam = len(text) + 4
    print('~' * tam)
    print(f'  {text}')
    print('~' * tam)


# Programa Principal
while True:
    header('SISTEMA DE AJUDA PyHELP')
    resp = str(input('Função ou Biblioteca > ')).strip()
    if resp.lower() == '':
        header('\033[0;36;41mATÉ LOGO!\033[m')
        break
