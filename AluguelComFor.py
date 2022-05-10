valordiv = int(input())
mensal = int(input())
c = 1
for x in range(valordiv, 0, -mensal):
    print(f'pagamento: {c}')
    print(f'antes = {x}')
    if x - mensal >= 0:
        print(f'depois = {x - mensal}')
    else:
        print(f'depois = 0')
    print('-' * 5)
    c += 1