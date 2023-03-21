#5
conta = int(input('Digite sua conta do banco: '))
saldo = int(input('Digite seu saldo em conta: '))
debito = int(input('Digite quanto voce tem de debito: '))
credito = int(input('Digite quanto voce tem de credito: '))

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print(f'Saldo positivo: {saldo_atual} ')
else:
    print(f'Saldo negativo: {saldo_atual}')