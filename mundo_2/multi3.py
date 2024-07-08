#contagem multiplos de 3
soma = 0
cntg_mult_3 = 0
mult_3 = []

#intervalo de 1 a 500
for numero in range(1, 501, 2):
    #se o número for multiplo de 3
    if numero % 3 == 0:
        #incrementa o contador
        cntg_mult_3 += 1
        #adiciona o número multiplo de 3 à lista
        mult_3.append(numero)
        soma += numero

#imprimir multiplos de 3 
print(f'Os numeros multiplos de 3 entre 1 e 500 sao: {mult_3}')
print(f'Existem {cntg_mult_3} numeros multiplos de 3 nesse intervalo.')
print(f'A soma de todos os valores solicitados é {soma}')