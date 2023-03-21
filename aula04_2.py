#2
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

soma = nota1 + nota2
media = soma / 2

if media >= 6:
    print (f'Aprovado! Media: {media}')
else:
    print (f'Reprovado. Media: {media}')