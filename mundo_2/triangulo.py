#lendo dados
r1, r2, r3 = map(float , input('DIGITE O VALOR DAS TRES RETAS:').split())

#analisando dados

if r1 < r2 + r2 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima pode formar um triângulo', end='')
    if r1 == 2 and r2 == 3:
        print('EQUILÁTERO')
    if r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALEO')
    else:
        print('ISÓCELES')
else:
    print('As retas acimas não podem formar um trinângulo')
