from random import randint


def int_input(text):
    try:
        num = abs(int(input(f'{text} ').strip()))
    except(TypeError, ValueError, KeyError):
        print('\033[1;31mDados inseridos de forma incorreta\033[m')
        return -1
    return num


def tira_carta():
    global baralho
    if len(baralho) > 0:
        naipe = ''
        while naipe not in baralho.keys():
            naipe = naipes[randint(0, 3)]
        valor = randint(0, len(baralho[naipe])-1)
        carta = baralho[naipe][valor]
        del baralho[naipe][valor]
        if len(baralho[naipe]) == 0:
            del baralho[naipe]
        return [naipe, carta]
    return -1


class Jogador:
    def __init__(self, nome: str):
        while nome == '':
            print('\033[1;31mDigite um nome válido!\033[m')
            nome = input('Digite novamente: ').strip()
        self.nome = nome
        self.valor = 0
        self.cartas = []

    def get_nome(self):
        return self.nome


class Computador(Jogador):
    def __init__(self):
        super().__init__('Computador')

    def get_nome(self):
        return f'\033[35m{self.nome}\033[m'


# Constante ou variáveis importantes
baralho = {
    'Paus':    ['Ás', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'],
    'Ouros':   ['Ás', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'],
    'Copas':   ['Ás', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'],
    'Espadas': ['Ás', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'],
}
naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']

# Programa principal
print()
print('\033[1;30;44m' + '~=' * 30, end='\033[m\n')
print(' '*18 + '\033[1;34mBlackjack, o jogo do 21\033[m')
print('\033[1;30;44m' + '~=' * 30, end='\033[m\n\n')

while True:
    num_jogadores = int_input('Quantos jogadores irão jogar? (máximo 5)')
    if num_jogadores == 0:
        print('\033[1;31mDigite um valor válido [>=1]\033[m')
    elif num_jogadores == 1:
        print('\033[36mVocê jogará contra o computador\033[m')
        break
    elif 1 < num_jogadores <= 5:
        break
    elif num_jogadores > 5:
        print('\033[37mO número máximo de jogadores é 5! Considerando 5 jogadores\033[m')
        num_jogadores = 5
        break

jogadores = []
for i in range(num_jogadores):
    jogadores.append(Jogador(input(f'Nome do Jogador {i+1}: ').strip()))

if num_jogadores == 1:
    jogadores.append(Computador())
