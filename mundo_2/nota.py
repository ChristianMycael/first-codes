#LENDO DADOS
nota1 = float(input('DIGITE A PRIMEIRA NOTA: '))

nota2 = float(input('DIGITE A SEGUNDA NOTA:'))


#CALCULO MEDIA

media = (nota1 + nota2) / 2

#RESULTADOS 

if media < 5:
    print(f'A média do aluno foi de {media} e está de REPROVADO.')

elif media > 5 and media < 6.9:
    print(f'A média do aluno foi de {media} e o aluo está de RECUPERAÇÃO.')

else:
    print(f'A média do aluno foi de {media} e o aluno está APROVADO.')