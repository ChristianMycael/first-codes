#lendo dados
casa = float(input('Valor da casa:'))
salario = float(input('Salario do comprador:'))
financiamento = int(input('Quantos anos de financiamento:'))

#calculo dos 30% do salario 

limite = salario * 0.3

#dados das prestações

prestacao = casa / (financiamento * 12)

#emprestimo 
if prestacao <= limite:
    print(f'PARA PAGAR UMA CASA DE {casa} EM {financiamento} ANOS A PRESTAÇÃO SERÁ DE {prestacao:.2f}\nEMPRESTIMO CONCEDIDO')
else:
    print(f'PARA PAGAR UMA CASA DE {casa} EM {financiamento} ANOS A PRESTAÇÃO SERÁ DE {prestacao:.2f}\nEMPRESTIMO NEGADO')