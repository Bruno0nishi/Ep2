from questoes import*
from trasformabase import*

premio = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
pulo = 3
ajuda = 2 

magenta = '\033[35m'


print('Olá! Você está na Fortuna DesSoft e terá a opurtunidade de enriquecer!')
nome = input('\nQual é o seu nome?')
print('\nok {0}, você tem direito a pular 3 vezes e 2 ajudas!'.format(nome.upper()))
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')

comeca = input('\naperte ENTER para continuar...')

jogo = True 

for termo in valida_questoes(questao):

    if termo != {}:
        jogo = False
        print("Possui questões invalidadas:")
        
while jogo == True :
    if comeca == '':
        jogo = False 
        print('\nO jogo já vai começar! Lá vem a primeira questão!')
        print('Vamos começar com questões do nível FACIL!')
        Continuar =input('\nAperte ENTER para continuar...')
        