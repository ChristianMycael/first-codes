from datetime import date

#lendo dados
atual = date.today().year
nasc =  int(input('DIGITE O ANO DE NASCIMENTO:'))
idade = atual - nasc

#classificando por idade

if idade < 9:
    print('Categoria: MIRIM.')

elif idade <= 14:
    print(' Categoria: INFANTIL.')

elif idade <=19:
    print('Categoria: JÚNIOR.')

elif idade <= 25:
    print('Categoria: SÊNIOR.')

else:
    print('Categoria: MASTER.')