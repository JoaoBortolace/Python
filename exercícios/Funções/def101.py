from datetime import datetime


def voto(ano_nascimento=2000):
    global idade
    idade = datetime.today().year - ano_nascimento
    if idade < 16:
        return 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    return 'VOTO OBRIGATÓRIO'


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
idade = 0
cond = voto(nasc)
print(f'Com {idade} anos: {cond}.')
