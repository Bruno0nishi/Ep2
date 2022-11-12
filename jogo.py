from questoes import*
from trasformabase import*
from funcoes import* 

dinheiro = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
rodada = 0
pulo = 3
ajuda = 2 

questao_para_jogo = transforma_base(questao)
usadas = []
numero = 0 




print('Olá! Você está na Fortuna DesSoft e terá a opurtunidade de enriquecer!')
nome = input('\nQual é o seu nome?')
print('\nok {0}, você tem direito a pular 3 vezes e 2 ajudas!'.format(nome.upper()))
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')

comeca = input('\naperte ENTER para continuar...')

if comeca == '':
    print ("\nO jogo já vai começar! Lá vem a Primeira questão"'\n')
    print('Vamos começar com questões do nível FÁCIL.''\n')
continuar = input('Aperte ENTER para começar...')

jogo = True         
while jogo :
    
    # questões fáceis 
    if rodada <= 3:
        numero += 1 
        questao_sorteada = sorteia_questao(questao_para_jogo, 'facil')
        nova_questao = sorteia_questao_inedita(questao_para_jogo, 'facil', usadas)
        questao_jogada_texto = questao_para_texto(nova_questao ,numero )
        print(questao_jogada_texto)
    
    #questões médias   
    if rodada >3 and rodada <= 6 :
        numero +=1 
        questao_sorteada = sorteia_questao(questao_para_jogo, 'medio')
        nova_questao = sorteia_questao_inedita(questao_para_jogo, 'medio', usadas)
        questao_jogada_texto = questao_para_texto(nova_questao ,numero )
        print(questao_jogada_texto)
    
    if rodada > 6 and rodada <= 9 :
        numero +=1 
        questao_sorteada = sorteia_questao(questao_para_jogo, 'dificil')
        nova_questao = sorteia_questao_inedita(questao_para_jogo, 'dificil', usadas)
        questao_jogada_texto = questao_para_texto(nova_questao ,numero )
        print(questao_jogada_texto)
    
    