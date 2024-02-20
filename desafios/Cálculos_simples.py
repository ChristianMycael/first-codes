#passo um lendo dados de entrada
codigo_da_peca1, num_peca1, valor_unitario1 = map (float, input('DIGITE O CODIGO DA PEÇA, QUANTIDADE E VALOR:').split())
codigo_da_peca2, num_peca2, valor_unitario2 = map (float, input('DIGITE O CODIGO DA PEÇA, QUANTIDADE E VALOR:').split())

#passo dois calculo 

total_pagar =  (num_peca1 * valor_unitario1) + (num_peca2 * valor_unitario2)


#passo tres mostra o total a pagar 

print(f'VALOR A PAGAR: R$ {total_pagar:.2F}')
