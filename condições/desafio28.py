#PARTE 1 / importar biblioteca 
from random import randint
from time import sleep

#PARTE 2 / computador vai "pensar"
computador = randint(0, 5)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

#parte 3 / jogador tenta adinvinhar 
jogador = int(input('Em que número eu pensei:'))
print('PROCESSANDO..') 
sleep(3)

#parte 4 /  jogador vs computador
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')

else:
    print(f'Ganhei! Eu pensei no número {computador} e não no número {jogador}')