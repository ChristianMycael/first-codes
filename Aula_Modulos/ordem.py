import random

aluno_1 = input('digite o numero e nome do aluno')
aluno_2 = input('digite o numero e nome do aluno')
aluno_3 = input('digite o numero e nome do aluno')
aluno_4 = input('digite o numero e nome do aluno')

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteio = random.shuffle(lista)

print(f'A ordem de apresentação é {sorteio}')