#parte 1 retas 
r1 ,r2 , r3 = map(float, input('DIGITE O VALOR DAS RETAS:').split())

#parte 2 
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('As retas acima podem formar um triângulo!')
else:
    print('As retas acima não podem formar um triângulo!')