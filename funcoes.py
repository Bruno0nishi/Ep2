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


def valida_questao(questao):
    dic = {}
    chaves = ["titulo", "nivel", "opcoes", "correta"]
    nivels = ["facil", "medio", "dificil"]
    letras = ["A", "B", "C", "D"]
    for chave in chaves:
        if chave not in questao:
            dic[chave] = "nao_encontrado"
    if len(questao) != 4:
        dic["outro"] = "numero_chaves_invalido"
    if chaves[0] in questao:
        if questao["titulo"].strip() == "":
            dic["titulo"] = "vazio"
    if chaves[1] in questao:
        if questao["nivel"] not in nivels:
            dic["nivel"] = 'valor_errado'
    if chaves[2] in questao:
        if len(questao["opcoes"]) != 4:
            dic["opcoes"] = 'tamanho_invalido'
        else:
            for option in letras:
                if option not in questao["opcoes"]:
                    dic["opcoes"] = "chave_invalida_ou_nao_encontrada"
            for option in letras:
                if questao["opcoes"][option].strip() == "":
                    if "opcoes" not in dic: 
                        dic["opcoes"] = {f'{option}': 'vazia'}
                    else:
                        dic["opcoes"][option]  = "vazia"
    if chaves[3] in questao:
        if questao["correta"] not in letras: 
            dic["correta"] = 'valor_errado'
    return dic


def sorteia_questao(dici, nivel):
    x = random.choice(dici[nivel])
    return x 
        

def sorteia_questao_inedita(dici, nivel, lista):
    T = True 
    while T:
        q = random.choice(dici[nivel])
        if q not in lista :
            T = False 
            lista.append(q)
        return q 

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
    #num = random.randint(1, 2)
    num = 1
    if num == 1:
        ajuda = random.choice(incorreto)
        return 'DICA:\nOpções certamente erradas: {0}'.format(opc[ajuda])
    if num == 2:
        ajuda = random.choice(incorreto)
        incorreto.remove(ajuda)
        ajs2 = random.choice(incorreto)
        return 'DICA:\nOpções certamente erradas: {0} e {1}'.format(opc[ajuda], opc[ajs2])