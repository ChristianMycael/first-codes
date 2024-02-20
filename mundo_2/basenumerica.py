#lendo dados 

num =  int(input('DIGITE UM NÚMERO INTEIRO:'))

#seleção de conversao
print(''' ESCOLHA UMA DAS BASES DE CONVERSÃO:
      [ 1 ] CONVERTER PARA BINÁRIO
      [ 2 ] CONVERTER PARA OCTAL
      [ 3 ] CONVERTER PARA HEXADECIMAL''')

#seleção 

opcao =  int(input('Sua opção:'))

#conversao binario, octal e hexadecimal
if opcao == 1:
    binario = bin(num)
    print(f'{num} convertido para binário é igual a {binario [2:]}')
elif opcao == 2:
    octal = oct(num)
    print(f'{num} convertido para octal é igual a {octal [2:]}')
elif opcao == 3:
    hexadecimal = hex(num)
    print(f'{num} convertido para hexadecimal é igual a {hexadecimal [2:]}')
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')






