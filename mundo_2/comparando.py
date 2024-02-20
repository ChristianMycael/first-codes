num1 = int(input('DIGITE UM NÚMERO: '))
num2 = int(input('DIGITE OUTRO NÚMERO:'))

if num1 > num2:
    print(f'o numero {num1} é maior que o {num2} ')

elif num2 > num1:
    print(f'o numero {num2} é maior que o {num1}')

else:
    print('Não existe valor maior, os dois são iguais.')