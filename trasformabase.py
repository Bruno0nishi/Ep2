def transforma_base(lista):
    dicionario = {}
    lista_facil = []
    lista_medio = []
    lista_dificil = []
    for e in lista:
        if e['nivel'] =='facil':
            lista_facil.append(e)
            dicionario['facil'] = lista_facil
        elif e['nivel'] == 'medio':
            lista_medio.append(e)
            dicionario['medio'] = lista_medio
        else:
            lista_dificil.append(e)
            dicionario['dificil'] = lista_dificil
    return dicionario