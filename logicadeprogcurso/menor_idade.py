idade = int ( input (' Digite sua idade: '))

if idade < 18:
    print('Você ainda é um(a) menor(a)')

elif idade >= 18 and idade < 60:
    print('Você é um(a) adulto')

elif idade >= 60:
    print('Você é um(a) idoso(a)')

else:
    print('Idade inválida')