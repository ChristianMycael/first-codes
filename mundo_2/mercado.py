#PARTE 1 
print('{:=^40}'.format(' MERCADINHO DO RUIVO '))
preco = float (input(' Preço das compras R$: '))

# PARTE 2 
print('''FORMAS DE PAGAMENTO
      [ 1 ] À VISTA DINHEIRO/CHEQUE
      [ 2 ] À VISTA NO CARTÃO
      [ 3 ] 2X NO CARTÃO
      [ 4 ] 3X OU MAIS NO CARTÃO''')
opcao = int ( input('QUAL A OPÇÃO? '))

#PARTE 3 
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int (input('Quantas parcelas:'))
    parcela =  total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = preco
    print('OPÇÃO INVÁLIDA. Tente novamente!')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')


