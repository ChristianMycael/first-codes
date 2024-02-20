from datetime import date

# LENDO DADOS
atual = date.today().year

ano =  int(input('DIGITE O ANO DE NASCIMENTO: '))

idade = atual - ano

if idade == 18:
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
    print('Você está na idade certa para se alistar')
elif idade < 18:
    saldo  = 18 - idade
    anos = atual + saldo
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
    print(f'ainda falta {saldo} anos para se alistar\nSeu alistamento será em {anos}')

else:
    saldo = idade - 18
    anos = atual - saldo
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
    print(f' Você já deveria ter se alistado há {saldo} anos.\nSeu alistamento foi em {anos}')