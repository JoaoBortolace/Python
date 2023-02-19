def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print(voto(int(input('-' * 30 + '\nEm que ano você nasceu? '))))
