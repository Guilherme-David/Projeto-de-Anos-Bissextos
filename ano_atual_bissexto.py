from datetime import date
ANO_ATUAL = date.today().year

def MensagemAnoAtual(ano_atual=ANO_ATUAL):
    return f'Estamos no ano {ano_atual},'

def anoAtualEhBissexto(ano_atual=ANO_ATUAL):
    if ano_atual % 4 == 0 and ano_atual %100 != 0 or ano_atual % 400 == 0:
        return 'O ano atual É BISSEXTO'
    else:
        return 'O ano atual NÃO É BISSEXTO'
