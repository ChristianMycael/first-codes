#PARTE 1
d = float(input('QUAL A DISTÂNCIA EM KM:'))

#PARTE 2
if d <= 200:
    p = d * 0.50
    print (f'A passagem custara {p:.2f}')
else:
    d > 200
    p = d * 0.45
    print(f'A passagem custara {p:.2f}')