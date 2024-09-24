sexo = input('digite seu sexo:')
h = float (input('digite sua altura: '))

if sexo.lower() == 'homem':
    peso_homen = (72.7 * h) - 58
    print(f'peso ideal: {peso_homen}')

elif sexo.lower() == 'mulher':
        peso_mulher = (62.1 * h) - 44
        print(f'peso ideal: {peso_mulher}')

else:
    print('sexo invalido')

