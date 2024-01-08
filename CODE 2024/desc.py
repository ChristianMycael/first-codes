#12

valor = float(input('digite o valor'))

percentual_desconto = int(input('digite o valor:'))

desconto = valor * (percentual_desconto / 100)
novo_valor = valor - desconto

print (f'O desconto é {desconto} \nO valor apos o desconto é de {novo_valor}')