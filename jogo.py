from questoes import*
from trasformabase import*
from funcoes import* 

dinheiro = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
rodada = 0
pulo = 3
ajuda = 2 

ajuda_rodada = 1 

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
    
    #questoes difíceis 
    if rodada > 6 and rodada <= 9 :
        numero +=1 
        questao_sorteada = sorteia_questao(questao_para_jogo, 'dificil')
        nova_questao = sorteia_questao_inedita(questao_para_jogo, 'dificil', usadas)
        questao_jogada_texto = questao_para_texto(nova_questao ,numero )
        print(questao_jogada_texto)
        
    resposta = input('qual a sua resposta?: ')
    # pulos   
    if resposta == 'pular' and pulo>= 1 :
        pulo -=1
        print(f'você ainda tem {pulo} pulos')
    if resposta == 'pular' and pulo <= 0 :
        print('você não tem mais pulos.')
        resposta = input('qual a sua resposta?: ')
        if resposta == 'pular':
            print('Que pena! Você errou e vai sair pobre')
            break 
    # ajudas 
    if resposta == 'ajuda' and ajuda_rodada != 0 :
        questao_aleatoria = questao_jogada_texto['opcoes']['A']
        receber_ajuda = gera_ajuda(questao_sorteada)
        ajuda_rodada -= 1 
        
        if ajuda < 0 :
            print ('Não deu! Você  não tem mais direito a ajudas !')
            continuar = input('Aperte ENTER para começar...')
            if continuar == '':
                print('')
                
        if ajuda == 1 :
            print('OK, lá vem ajuda')   
            print('atenção você não tem mais direito a ajudas')  
            continuar = input('Aperte ENTER para começar...')
            if continuar == '':
                print('')
            print(f'DICA''\n''opções certamente erradas {questao_aleatoria}')
            continuar = input('Aperte ENTER para começar...')
            if continuar == '':
                print('')
                
        if ajuda == 2 :
            print('OK, lá vem ajuda! Você tem direito a mais uma ajuda.') 
            continuar = input('Aperte ENTER para começar...')
            if continuar == '':
                print('') 
            print(f'DICA''\n''opções certamente erradas {questao_aleatoria}')
            continuar = input('Aperte ENTER para começar...')
            if continuar == '':
                print('')
        print(questao_jogada_texto) 
        
        if ajuda_rodada == 0 :
            print('Você não tem direito a mais ajudas.')
            resposta = input('qual a sua resposta?: ')
            if resposta == 'ajuda':
                print ('Que pena! Você errou e vai sair pobre')
                break
            
    
            
            
            
            
            
        