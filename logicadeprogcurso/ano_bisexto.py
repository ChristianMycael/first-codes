#importação
from datetime import date

#escolhendo o ano

ano = int(input('Digite o ano: '))

#verificando se é bissexto
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100!=0 or ano % 400 == 0:
     print(f'{ano} é um ano bissexto')

else:
    print(f'{ano} não é um ano bissexto')
