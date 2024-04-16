def calcularAnosBissextos(lista_bissextos=list, ano_inicial=int, ano_final=int):
    for ano in range (ano_inicial, ano_final + 1):
        if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0:
            lista_bissextos.append(ano)
    return lista_bissextos
        