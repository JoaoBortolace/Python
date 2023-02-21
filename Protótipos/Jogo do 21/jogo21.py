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
        valor = randint(0, len(baralho[naipe]) - 1)
        carta = baralho[naipe][valor]
        del baralho[naipe][valor]
        if len(baralho[naipe]) == 0:
            del baralho[naipe]
        return [naipe, carta]
    return -1


class Jogador:
    def __init__(self, nome: str, aposta: bool):
        while nome == '':
            print('\033[1;31mDigite um nome válido!\033[m')
            nome = input('Digite novamente: ').strip()
        self.__nome = nome
        if aposta:
            try:
                self.__aposta = float(input('Qual a sua aposta? R$').replace(',', '.'))
            except(TypeError, ValueError, KeyError):
                print('\033[1;31mValor inválido, considerando com R$0\033[m')
                self.__aposta = 0.0
        self.__valor = 0
        self.__cartas = []

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        self.__calcula_valor()
        return self.__valor

    def get_aposta(self):
        return self.__aposta

    def get_cartas(self):
        return self.__cartas

    def receber_cartas(self, quant: int):
        for c in range(quant):
            tirada = tira_carta()
            if tirada == -1:
                return False
            self.__cartas.append(tirada)
        return True

    def __calcula_valor(self):
        v = 0
        for c in self.__cartas:
            v += valores[str(c[1])]
        self.__valor = v


class Computador(Jogador):
    def __init__(self):
        super().__init__('Computador', False)

    def get_nome(self):
        return f'\033[35m{self.__nome}\033[m'


# Constante ou variáveis importantes
baralho = {
    'Paus': ['Ás', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'],
    'Ouros': ['Ás', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'],
    'Copas': ['Ás', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'],
    'Espadas': ['Ás', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei']}
naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
valores = {'Ás': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valete': 10,
           'Dama': 10, 'Rei': 10}

# Programa principal
print()
print('\033[1;30;44m' + '~=' * 30, end='\033[m\n')
print(' ' * 18 + '\033[1;34mBlackjack, o jogo do 21\033[m')
print('\033[1;30;44m' + '~=' * 30, end='\033[m\n\n')

while True:
    num_jogadores = int_input('Quantos jogadores irão jogar? (máximo 12)')
    if num_jogadores == 0:
        print('\033[1;31mDigite um valor válido [>=1]\033[m')
    elif num_jogadores == 1:
        print('\033[36mVocê jogará contra o computador\033[m')
        break
    elif 1 < num_jogadores <= 12:
        break
    elif num_jogadores > 12:
        print('\033[37mO número máximo de jogadores é 12! Considerando 12 jogadores\033[m')
        num_jogadores = 12
        break

jogadores = []
for i in range(num_jogadores):
    if num_jogadores == 1:
        jogadores.append(Jogador(input(f'Nome do Jogador {i + 1}: ').strip(), False))
    else:
        jogadores.append(Jogador(input(f'Nome do Jogador {i + 1}: ').strip(), True))

if num_jogadores == 1:
    jogadores.append(Computador())

# Ditribuição das cartas
for j in jogadores:
    if not j.receber_cartas(2):
        print('\033[1;31mNão há mais cartas no baralho...\033[m')
