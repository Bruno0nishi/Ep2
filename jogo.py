from questoes import*
from trasformabase import*
from funcoes import* 

dinheiro = 0
rodada = 0
pulo = 3
ajuda = 2
facil = 0 

questao_para_jogo = transforma_base(questao)
numero = 0 



print('Olá! Você está na Fortuna DesSoft e terá a opurtunidade de enriquecer!')
nome = input('\nQual é o seu nome?')
print('\nok {0}, você tem direito a pular 3 vezes e 2 ajudas!'.format(nome.upper()))
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pular" e "parar"!')

comeca = input('\naperte ENTER para continuar...')

if comeca == '':
    print ("\nO jogo já vai começar! Lá vem a Primeira questão"'\n')
    print('Vamos começar com questões do nível FÁCIL.''\n')
continuar = input('Aperte ENTER para começar...')

        
jogo = True         
while jogo :
    usadas = []
    
# questões fáceis 
    if dinheiro>= 0 and dinheiro < 10000:
        numero += 1 
        questao_sorteada = sorteia_questao(questao_para_jogo, 'facil')
        nova_questao = sorteia_questao_inedita(questao_para_jogo, 'facil', usadas)
        questao_jogada_texto = questao_para_texto(nova_questao ,numero )
        print(questao_jogada_texto)
    
    #questões médias   
    if dinheiro >= 10000 and dinheiro < 100000 :
        numero +=1 
        questao_sorteada = sorteia_questao(questao_para_jogo, 'medio')
        nova_questao = sorteia_questao_inedita(questao_para_jogo, 'medio', usadas)
        questao_jogada_texto = questao_para_texto(nova_questao ,numero )
        if nova_questao not in usadas :  
            usadas.append(nova_questao)
        print(questao_jogada_texto)
    
    #questoes difíceis 
    if dinheiro >= 100000 and dinheiro < 1000000 :
        numero +=1 
        questao_sorteada = sorteia_questao(questao_para_jogo, 'dificil')
        nova_questao = sorteia_questao_inedita(questao_para_jogo, 'dificil', usadas)
        questao_jogada_texto = questao_para_texto(nova_questao ,numero )
        if nova_questao not in usadas :  
            usadas.append(nova_questao)
        print(questao_jogada_texto)
        
        
    resposta = input('qual a sua resposta?: ')
    ajuda_rodada = 1
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
        receber_ajuda = gera_ajuda(nova_questao)
        ajuda_rodada -= 1
                
        if ajuda == 1 :
            print('OK, lá vem ajuda')   
            print('atenção você não tem mais direito a ajudas')  
            continuar = input('Aperte ENTER para continuar...')
            if continuar == '':
                print('')
            print(f'{receber_ajuda}')
            continuar = input('Aperte ENTER para continuar...')
            if continuar == '':
                print('')
                
        if ajuda == 2 :
            print('OK, lá vem ajuda! Você tem direito a mais uma ajuda, mas não nessa questão.') 
            continuar = input('Aperte ENTER para continuar...')
            if continuar == '':
                print('') 
            print(f'{receber_ajuda}')
            continuar = input('Aperte ENTER para continuar...')
            if continuar == '':
                print('')
        print(questao_jogada_texto) 
        
        if ajuda_rodada == 0 :
            print('Você não tem direito a mais ajudas.')
            resposta = input('qual a sua resposta?: ')
            if resposta == 'ajuda':
                print ('Que pena! Você errou e vai sair pobre')
                break
        ajuda -=1
    if resposta=='ajuda' and ajuda <= 0 :
            print ('Não deu! Você  não tem mais direito a ajudas !')
            continuar = input('Aperte ENTER para continuar...')
            if continuar == '':
                print('')
    if resposta == nova_questao['correta']:
        rodada += 1
        # PONTUAÇÃO A CADA QUESTÃO 
        if rodada == 1:
            dinheiro = 1000
            
        elif rodada== 2:
            dinheiro = 5000
        elif rodada == 3:
            dinheiro = 10000
            print('HEY! Você passou para o nível MEDIO!')
        elif rodada == 4:
            dinheiro = 30000
        elif rodada == 5:
            dinheiro  = 50000
        elif rodada == 6:
            dinheiro = 100000
            print('HEY! Você passou para o nível DIFICIL!')
        elif rodada == 7:
            dinehiro = 300000
        elif rodada == 8:
            dinheiro = 500000
        elif rodada == 9:
            print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais! ')
            dinheiro = 1000000
            break
        print(f'Voce acertou!! Seu premio atual e de R$ {dinheiro}')
        continuar = input('Aperte ENTER para continuar...')
        if continuar == '':
            print('')
    if resposta == 'parar':
        break
    if resposta != 'ajuda' and resposta != nova_questao['correta'] and resposta != 'pular':
        print('Que pena! Voce errou e vai sair pobre.')
        break

            
            
            
            
        