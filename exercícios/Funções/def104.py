def leia_int(text):
    print('-' * 30)
    while True:
        num_temp = str(input(text)).strip()
        if num_temp == '':
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            e = True
            for i in range(0, len(num_temp)):
                if num_temp[i].isalpha() or num_temp[i] in '%$,./*;:?' or (num_temp[i] in '+-' and i > 0):
                    print('\033[31mERRO! Digite um número inteiro válido.\033[m')
                    e = False
                    break
            if e:
                return int(num_temp)


# Programa Principal
n = leia_int('Digite um número: ')
print(f'Você digitou {n}')
