#15

a = int(input('digite um valor de dias:'))
km = float(input('digite quantos km rodado:'))


p = (60 * a) + (0.15 * km)


print (f'Total a pagar é de R${p:.2f}')