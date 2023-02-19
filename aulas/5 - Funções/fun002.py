# Podemos empacotar parâmetros
# Empacotar nos permite a passagem de um número indeterminados de parâmetro para a função
# Essas valores serão passados como uma tupla
# Ex: uma chamada passa 2, outra passa 5, outra 3, ...
def contador(*num):  # * para indicar empacotamento
    for v in num:
        print(v, end=' ')
    print(f'São ao todo {len(num)} elementos', end=' ')
    print('FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 8, 2)
