#LENDO DADOS

altura = float(input('DIGITE A SUA ALTURA: '))
peso = float(input('DIGITE O SEU PESO:'))

#CALCULO

imc = peso / (altura ** 2)

#analisando 

if imc < 18.5:
    print(f'VOCÊ ESTÁ ABAIXO DO PESO\nSEU IMC É DE:{imc:.2f}')
elif 18.8 <= imc < 25:
    print(f'VOCÊ ESTÁ NO PESO IDEAL\nSEU IMC É DE: {imc:.2f}')
elif 25 <= imc < 30:
    print(f'VOCÊ ESTÁ COM SOBREPESO\nSEU IMC É DE:{imc:.2F}')
elif 30 <= imc < 40:
    print(f'VOCÊ ESTÁ OBESIDADE\nSEU IMC É DE:{imc:.2f}')
else:
    print(f'VOCÊ ESTÁ EM OBESIDADE MÓRBIDA\nSEU IMC É DE:{imc:.2F}')