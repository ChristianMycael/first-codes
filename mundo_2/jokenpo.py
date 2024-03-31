#PARTE 1 
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int (input('Qual é sua jogada? '))
print('JO...')
sleep (1)
print('KEN...')
sleep (1)
print('PO!!!')
print('-=' *11)
print(f'computador jogou {itens[computador]}')
print(f'jogador jogou {itens[jogador]}')
print('-=' *11)

#PARTE 2 

if computador == 0:  #PEDRA
    if jogador == 0:
        print('EMPATOU')

    elif jogador == 1:
        print('JOGADOR VENCEU')
    
    elif jogador == 2:
        print('JOGADOR PERDEU')
    
    else:
        print('JOGADA INVÁLIDA.')

elif computador == 1: #PAPEL
    if jogador == 0:
        print('JOGADOR PERDEU')

    elif jogador == 1:
        print('EMPATOU')
    
    elif jogador == 2:
        print('JOGADOR VENCEU')
        
    else:
        print('JOGADA INVÁLIDA.')

elif computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')

    elif jogador == 1:
        print('JOGADOR PERDEU')
    
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('JOGADA INVÁLIDA.')
