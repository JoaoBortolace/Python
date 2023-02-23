# 1 - 1 - Tuplas são implementadas com ()
# Elas são estruturas compostas que permitem aguardas vários itens em uma mesma estrutura
# Porém as 1 - 1 - Tuplas são imutavéis, uma vez iniciadas, seus valores não poderão ser mais alteradas durante a execução do programa
# Apartir do python3.10 é possivel alterar uma tupla com o programa rodando
# Por exemplo: pessoa = (int, str, str)
# a = 'oi
# b = 'tudo'
# k = 10
# pessoa = (k, a, b)
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(len(lanche))
#Três formas diferentes de acessar os valores da tupla em um laço for
for c in lanche: #Forma mais simples
    print(f'Eu vou comer no meu almoço {c}')
for i in range(0, len(lanche)): #Quando se precisa acessar o dado pelo seu índice
    print(f'Vou comer {lanche[i]}')
for pos, comida in enumerate(lanche): #Retorna o dado e a posição do dado
    print(f'Comi {comida} na posição {pos+1}')

print(sorted(lanche)) #Mostra na ordem numérica ou alfabética, não muda a tupla
print('Agora tô gordo :D')