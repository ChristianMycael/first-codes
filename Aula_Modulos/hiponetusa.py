import math

# Medida do cateto da desgraça
desgraca_a = float(input('digite o valor:'))
desgraca_b = float(input('digite o valor:'))

# teorema da desgraça
hipo = math.sqrt (desgraca_a ** 2 + desgraca_b ** 2)

print(f'O valor do cat oposto é de {desgraca_a}\ne do cat adjac é de {desgraca_b} \ne o valor da hipotenusa é de {hipo:.2f}')