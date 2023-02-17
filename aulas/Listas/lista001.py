# Listas são estruturas compostas assim como as Tuplas
# Elas permitem agurdar diferentes dados em uma mesma estrutura
# Porém, as listas diferentemente das Tuplas, permitem alterar seus dados durante a execução
num = [2, 3, 5, 7]  # Listas são implementas atráves de chaves []
print(num)
num.append(3)  # Esta é uma forma possível adicionar dados a lista, ele adicionará o dado no final da lista
print(num)
num.insert(2, 0)  # Adiciona o dado na posição determinada pelo primeiro parâmetro e move os demais para direita
print(num)
num.sort()  # Ordena a lista em ordem numérica ou alfanumérica, ele modifica a lista
print(num)
num.sort(reverse=True)  # Orderna na ordem inversa do sorted convencional
print(num)
print(f'Esta lista tem {len(num)} elementos.')  # O método len retorna o tamanho da lista
num.pop()  # Remove o último elemento, quando está sem parâmetro
print(num)
num.pop(2)  # Remove o dado da posição indicada pelo parâmetro
print(num)
num.append(5)
print(num)
num.remove(5)  # Remove a primeira ocorrência do dado indicado pelo parâmetro
# Caso não exita o valor na lista ele retornará um erro, para contornar isso, pode-se testar a existencia do valor
if 4 in num:  # Verifica a exitência do dado na lista
    num.remove(4)  # Se há, o valor na lista, ele será removido
else:
    print('Não achei o número indicado')
print(num)
