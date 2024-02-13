#PARTE 1 escolha dos numeros
n1, n2, n3 = map(int, input('DIGITE TRES NUMERO:').split())

#PARTE 2 verificando menor numero 
menor =  n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

#parte 3 verificando maior numero 
maior = n1 
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

#parte 4 mostrando maior e menor numero
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')