from datetime import date
#parte 1 escolha do ano
ano = int(input('QUE ANO QUER ANALISAR? Coloque 0 para analisar o ano atual:'))

#PARTE 2 BISSEXTO OU NÃO 
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto')