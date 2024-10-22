#contador 
contagem_pares = 0
numeros_pares = []

#intervalo de 1 a 50
for numro in range(1, 51):
    #se o número for par
    if numro % 2 == 0:
        #incrementa o contador
        contagem_pares += 1
        #adiciona o número par à lista
        numeros_pares.append(numro)

#imprime a contagem
print(f'Existem {contagem_pares} números pares no intervalo de 1 a 50.')

#imprime a lista de números pares

print('Os números pares são:', numeros_pares)


