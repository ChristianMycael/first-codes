#parte 1 usúario digitar um número
n = int(input('DIGITE UM NúMERO: '))

#parte 2 resto da divisao

r = n % 2

#parte 3 ele é par ou ímpar 
if r == 0:
    print(f'O número {n} é par')
else:
    print(f'o número {n} é ímpar')