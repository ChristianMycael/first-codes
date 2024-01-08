#13

salario = float(input('digite o valor:'))
percentual_aumento = 15

aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento

print (f'O aumento foi de {aumento}\nO total foi de {novo_salario:.3f}')