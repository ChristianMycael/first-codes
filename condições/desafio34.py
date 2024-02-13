#PARTE 1 
s = float(input('DIGITE O VALOR R$:'))

#PARTE 2
if s > 1.250:
    p = 10
    a = s * (p / 100)
    ns = s + a
    print(f'Esse é o seu aumento {a} e seu novo salario {ns:.3f}')

#PARTE 3
else: 
    s <= 1.250
    p = 15
    a = s * (p / 100)
    ns = s + a
    print(f'Esse é seu aumento {a} e seu novo salario {ns:.3f} ')
