#lendo dados
salario_do_usuario = float( input('Digite seu salario:'))

#salario mininmo 

salario_min = 1420 

#calculando quantos salarios mininos o usuarios ganha

salarios_minimos = salario_do_usuario // salario_min

print (f'Você ganha {salarios_minimos} salario minimo.')