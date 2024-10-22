'''
ano = int ( input('digite o ano de nascimento: '))

idade = 2024 - ano

if idade >= 16 and idade <=17:
    print('você não é obrigado a votar esse ano')

elif idade >= 18 and idade <= 65:
    print('você é obrigado a votar esse ano')

else:
    print('você não é obrigado a votar esse ano')
'''

from datetime import date 

ano_atual = date.today().year

ano_nascimento = int(input('Digite o ano de nascimento: '))

idade = ano_atual - ano_nascimento

if idade >= 16 and idade <= 17:
    print('Você não é obrigado a votar esse ano')

elif idade >= 18 and idade <= 65:
    print('Você é obrigado a votar esse ano')

else:
    print('Você não é obrigado a votar esse ano')