'''
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
'''



#PARTE 1 escolha dos numeros
a =  int(input('Digite um valores: '))
b =  int(input('Digite um valores: '))
c = int(input('Digite um valores: '))

#função para calcular o maior entre dois numeros
def maior_ab(a, b):
    return (a + b +abs (a -b)) / 2

# maior entre a e b 
maior = maior_ab(a, b)

#maior entre c e o resultado de a + b 
maior = maior_ab(maior, c)

print(f'{maior} eh o maior')