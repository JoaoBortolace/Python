a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c)
print(len(c))
print(c.index(5, 2)) #Retorna a posição do parâmetro na tupla, o segundo parâmetro marca da onde a procura irá
# começar na tupla
print(c.count(5)) #Retorna quantas vezes o parâmentro aparece na tupla
print(sorted(c))
