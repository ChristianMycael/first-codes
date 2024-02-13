#parte 1 
v = int(input('digite a velocidade: '))

#parte 2
m = (v - 80) * 7 

#parte 3
if v > 80:
    print(f'Você foi multado por excesso de velocidade e ira pagar\numa multa de R${m:.2f}')

else:
    print('Você está no limite da via')