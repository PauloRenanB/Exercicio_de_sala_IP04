#6
estoque_atual = int(input('Digite o estoque atual: '))
max_estoque = int(input('Digite a capacidade maxima do estoque: '))
min_estoque = int(input('Digite a capacidade minima do estoque: '))

qnt_media = max_estoque + min_estoque / 2

if estoque_atual >= qnt_media:
    print('Não efetuar compra')
elif estoque_atual < qnt_media:
    print('Efetuar compra')