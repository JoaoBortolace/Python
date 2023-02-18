def leia_int(text=''):
    while True:
        num_temp = str(input(text)).strip()
        if num_temp == '':
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            e = 0
            for i in range(0, len(num_temp)):
                if num_temp[i].isalpha() or num_temp[i] in '%$,./*;:?' or (num_temp[i] in '+-' and i > 0):
                    print('\033[31mERRO! Digite um número inteiro válido.\033[m')
                    e = 1
            if e == 0:
                break
    num = int(num_temp)
    return num


# Programa Principal
n = leia_int('Digite um número: ')
print(f'Você digitou {n}')
