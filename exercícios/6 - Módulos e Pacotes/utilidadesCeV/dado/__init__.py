def leia_dinheiro(p):
    while True:
        preco = str(input(p)).replace(',', '.').strip()
        if preco == '':
            print('\33[1;31mERRO: Insira algum preço!\033[m')
        else:
            valido = True
            i = 0
            virgula = False
            while valido and i < len(preco):
                if preco[i].isalpha():
                    valido = False
                if preco[i] == '.':
                    if virgula:
                        valido = False
                    virgula = True
                i += 1
            if valido:
                break
            print(f'\33[1;31mERRO: "{preco}" é um preço inválido!\033[m')
    return float(preco)
