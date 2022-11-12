import random

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


def valida_questao(dici):
    retorno = {}
    num = 0


    if 'titulo' in dici:
        if len(dici["titulo"].strip()) == 0:
            retorno["titulo"] = 'vazio'
    else:
        retorno["titulo"] = 'vazio'


            
    if 'nivel' in dici:
        if dici["nivel"] == "facil":
            pass
        elif dici["nivel"] == "medio":
            pass
        elif dici["nivel"] == "dificil":
            pass
        else:
            retorno['nivel'] = 'valor_errado'
    else:
        retorno['nivel'] = 'valor_errado'

    num = 0
    dici_op = {}

    if 'opcoes' in dici:
        for x in dici["opcoes"]:
            num += 1
        if num != 4:
            retorno['opcoes'] = 'tamanho_invalido'
        else:
            indice = 0
            indice_vazio = 0
            for c,v in dici['opcoes'].items():
                if 'A' in c:
                    indice += 1
                    if len(v.strip()) == 0:
                        dici_op['A'] = 'vazia'
                        indice_vazio +=1
                if 'B' in c:
                    indice += 1
                    if len(v.strip()) == 0:
                        dici_op['B'] = 'vazia'
                        indice_vazio +=1
                if 'C' in c:
                    indice += 1
                    if len(v.strip()) == 0:
                        dici_op['C'] = 'vazia'
                        indice_vazio +=1
                if 'D' in c:
                    indice += 1
                    if len(v.strip()) == 0:
                        dici_op['D'] = 'vazia'
                        indice_vazio +=1
            if indice != 4:
                retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                if indice_vazio != 0:
                    retorno['opcoes'] = dici_op
    else:
        retorno['opcoes'] = 'chave_nao_encontrada'
        
    if 'correta' in dici:
        if dici["correta"] == "A":
            pass
        elif dici["correta"] == "B":
            pass
        elif dici["correta"] == "C":
            pass
        elif dici["correta"] == "D":
            pass
        else:
            retorno['correta'] = 'valor_errado'
    else:
        retorno['correta'] = 'nao_encontrado'

    if len(dici) != 4:
        retorno["outro"] ='numero_chaves_invalido'
    return retorno 


def valida_questoes(lista):
    retorno = {}
    lista_final = []
    num = 0
    for x in lista:
        print(x)
        num += 1
        retorno[num] = valida_questao(x)
        lista_final.append(retorno[num])
        
    return lista_final

def sorteia_questao(dici, nivel):
    lista_questoes = {}

    indice = 1
    for chave,valor in dici.items():
        if chave == nivel:
            for e in valor:
                lista_questoes[indice] = e
                indice += 1
    num = len(lista_questoes)
    return lista_questoes[random.randint(1,num)]

def sorteia_questao(dici, nivel):
    lista_questoes = {}

    indice = 1
    for chave,valor in dici.items():
        if chave == nivel:
            for e in valor:
                lista_questoes[indice] = e
                indice += 1
    num = len(lista_questoes)
    return lista_questoes[random.randint(1,num)]

def sorteia_questao_inedita(dici, nivel, lista):
    while True:
        questao = sorteia_questao(dici, nivel)
        if questao not in lista:
            lista.append(questao)
            break
    
    return questao

def questao_para_texto (D,ID):
    return ("----------------------------------------"
    '\n'
    "QUESTAO {0}"
    '\n'
    '\n'
    "{1}"
    '\n'
    '\n'
    "RESPOSTAS:"
    '\n'
    "A: {2}"
    '\n'
    "B: {3}"
    '\n'
    "C: {4}"
    '\n'
    "D: {5}"
    ).format(ID,D["titulo"],D["opcoes"]["A"],D["opcoes"]["B"],D["opcoes"]["C"],D["opcoes"]["D"])


def gera_ajuda(x):
    incorreto = []
    correto = x['correta']
    opc = x['opcoes']
    for i in opc.keys():
        if i != correto:
            incorreto.append(i)
    num = random.randint(1, 2)
    if num == 1:
        ajuda = random.choice(incorreto)
        return 'DICA:\nOpções certamente erradas: {0}'.format(opc[ajuda])
    if num == 2:
        ajuda = random.choice(incorreto)
        incorreto.remove(ajuda)
        ajs2 = random.choice(incorreto)
        return 'DICA:\nOpções certamente erradas: {0} e {1}'.format(opc[ajuda],opc[ajs2])

