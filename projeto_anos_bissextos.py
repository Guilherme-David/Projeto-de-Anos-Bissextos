import ano_atual_bissexto
import anos_bissextos

print(ano_atual_bissexto.MensagemAnoAtual())
print(ano_atual_bissexto.anoAtualEhBissexto())

print('SEQUÊNCIA DE ANOS BISSEXTOS')
ano_inicial = int(input('Quer começar por qual ano? '))
ano_final = int(input('Até que ano? '))

print(anos_bissextos.calcularAnosBissextos([], ano_inicial, ano_final))