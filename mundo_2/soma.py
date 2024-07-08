soma = 0 
cont = 0
for i in range(1, 7):
    i = int(input(f'Digite o {i} valor:'))
    if i % 2 == 0:
        cont += 1
        soma += i
print(f'voce informou {cont} numeros pares e a soma foi {soma}')